import os
import pyarrow.parquet as pq
import pandas as pd

def load_parquet_file(parquet_path):
    if not os.path.exists(parquet_path):
        print(f"No Parquet file found at '{parquet_path}'.")
        return None
    
    table = pq.read_table(parquet_path)
    df = table.to_pandas()
    return df

def transformation_file(customer_df,order_product_df,store_product_df, store_df, product_df):
    customer_df.drop(columns=['load_date', 'source'], inplace=True)
    order_product_df.drop(columns=['load_date', 'source'], inplace=True)
    store_product_df.drop(columns=['load_date', 'source'], inplace=True)
    store_df.drop(columns=['load_date', 'source'], inplace=True)
    product_df.drop(columns=['load_date', 'source'], inplace=True)

    # Realiza um join entre order_product_df e customer_df usando a coluna 'customer_id'
    transformed_df = pd.merge(order_product_df, customer_df, on='customer_id', how='left')
    
    # Realiza um join entre transformed_df e store_product_df usando a coluna 'store_store_product_id' e 'store_product_id'
    transformed_df = pd.merge(transformed_df, store_product_df, left_on='store_store_product_id', right_on='store_product_id', how='left')
    
    transformed_df = pd.merge(transformed_df, store_df, left_on='store_id', right_on='store_id', how='left')
    
    transformed_df = pd.merge(transformed_df, product_df, left_on='product_id', right_on='product_id', how='left')



    return transformed_df

# Carregar os arquivos Parquet
price_df = load_parquet_file("datalake/clean-data/csv-price-search/price_clean.parquet")
reviews_df = load_parquet_file("datalake/clean-data/api-sentiment-analyze/reviews_clean.parquet")
customer_df = load_parquet_file("datalake/clean-data/db-postgres-prod/customer/customer_clean.parquet")
order_product_df = load_parquet_file("datalake/clean-data/db-postgres-prod/order_product/order_product_clean.parquet")
product_df = load_parquet_file("datalake/clean-data/db-postgres-prod/product/product_clean.parquet")
store_product_df = load_parquet_file("datalake/clean-data/db-postgres-prod/store_product/store_product_clean.parquet")
store_df = load_parquet_file("datalake/clean-data/db-postgres-prod/store/store_clean.parquet")

# Realizar transformações nos dados
transformed_df = transformation_file(order_product_df, customer_df, store_product_df, store_df, product_df)

transformed_df.to_csv("teste.csv")

# Imprimir o resultado
print("Transformed DataFrame:")
print(transformed_df.head())
