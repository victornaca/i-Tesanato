import os
import pyarrow.parquet as pq
import pandas as pd
from datetime import datetime


def load_parquet_file_sales(parquet_path):
    if not os.path.exists(parquet_path):
        print(f"No Parquet file found at '{parquet_path}'.")
        return None
    
    table = pq.read_table(parquet_path)
    df = table.to_pandas()
    return df

def transformation_file_sales(customer_df,order_product_df,store_product_df, store_df, product_df):
    customer_df.drop(columns=['load_date', 'source'], inplace=True)
    order_product_df.drop(columns=['load_date', 'source'], inplace=True)
    store_product_df.drop(columns=['load_date', 'source'], inplace=True)
    store_df.drop(columns=['load_date', 'source'], inplace=True)
    product_df.drop(columns=['load_date', 'source'], inplace=True)

    transformed_df = pd.merge(order_product_df, customer_df, on='customer_id', how='left')
    
    transformed_df = pd.merge(transformed_df, store_product_df, left_on='store_store_product_id', right_on='store_product_id', how='left')
    
    transformed_df = pd.merge(transformed_df, store_df, left_on='store_id', right_on='store_id', how='left')
    
    transformed_df = pd.merge(transformed_df, product_df, left_on='product_id', right_on='product_id', how='left')
    
    transformed_df = transformed_df[['order_id', 'product_id', 'product_name', 'order_quantity', 
                                 'store_product_price', 'order_date', 'store_id', 'store_name', 
                                 'customer_id', 'customer_name']]

    transformed_df['store_product_price'] = transformed_df['store_product_price'].astype(float)
    
    transformed_df = transformed_df.rename(columns={
    'order_id': 'Order ID',
    'product_id': 'Product ID',
    'product_name': 'Product Name',
    'order_quantity': 'Quantity Order',
    'store_product_price': 'Product Price',
    'order_date': 'Date Order',
    'store_id': 'Store ID',
    'store_name': 'Store Name',
    'customer_id': 'Customer Buyer ID',
    'customer_name': 'Customer Buyer Name'
})
    
    transformed_df['Load Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    datasources = {
    'csv-price-search': 'parquet',
    'db-postgres-prod/customer': 'parquet',
    'db-postgres-prod/order_product': 'parquet',
    'db-postgres-prod/product': 'parquet',
    'db-postgres-prod/store_product': 'parquet',
    'db-postgres-prod/store': 'parquet'
    }

    transformed_df['Source'] = str(datasources)

    return transformed_df

def load_datawarehouse_sales(dataframe):
    excel_path = "datawarehouse/sales.xlsx"
    try:
        # Verificar se o DataFrame está vazio
        if dataframe.empty:
            print("DataFrame is empty. Cannot save to Excel.")
            return
        
        print("Transformed DataFrame:")
        print(dataframe.head())  # Imprimir as primeiras linhas do DataFrame
        
        dataframe.to_excel(excel_path, index=False)
        print(f"DataFrame saved as Excel file at '{excel_path}'.")
    except Exception as e:
        print(f"Error saving DataFrame to Excel: {e}")
