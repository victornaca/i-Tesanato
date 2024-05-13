import os
import pyarrow.parquet as pq
import pandas as pd
from datetime import datetime

def load_parquet_file(parquet_path):
    if not os.path.exists(parquet_path):
        print(f"No Parquet file found at '{parquet_path}'.")
        return None
    
    table = pq.read_table(parquet_path)
    df = table.to_pandas()
    return df

def transformation_file(reviews_df):
    reviews_df.drop(columns=['load_date', 'source'], inplace=True)
    
    transformed_df = reviews_df.rename(columns={
        'id': 'Review ID',
        'timestamp': 'Date Review',
        'text': 'Text',
        'customer_id': 'Customer Buyer ID',
        'customer_username': 'Customer Buyer Name',
        'product_id': 'Product ID',
        'product_name': 'Product Name',
        'sentiment_label': 'Sentiment Predicted',
        'sentiment_score': 'Score'
    })
    
    transformed_df['Load Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    datasources = {
    'api-sentiment-analyze': 'parquet',
    }

    transformed_df['Source'] = str(datasources)
    
    # Formatar a data para o formato Excel
    transformed_df['Date Review'] = transformed_df['Date Review'].dt.strftime('%Y-%m-%d %H:%M:%S')
    
    return transformed_df

def load_datawarehouse(dataframe):
    excel_path = "datawarehouse/sentiment_analyst.xlsx"
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
