import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import shutil
from datetime import datetime

def convert_json_to_parquet():
    json_directory = "datalake/landing/api-sentiment-analyze/new"
    parquet_directory = "datalake/pre-process/api-sentiment-analyze/new"
    old_directory = "datalake/landing/api-sentiment-analyze/old"
    
    if not os.path.exists(json_directory):
        print(f"The source directory '{json_directory}' does not exist.")
        return
    
    if not os.path.exists(parquet_directory):
        os.makedirs(parquet_directory)
    
    json_files = [f for f in os.listdir(json_directory) if f.endswith('.json')]
    
    if not json_files:
        print(f"No JSON files found in the directory '{json_directory}'.")
        return
    
    for json_file in json_files:
        json_path = os.path.join(json_directory, json_file)
        parquet_file = os.path.splitext(json_file)[0] + ".parquet"
        parquet_path = os.path.join(parquet_directory, parquet_file)
        
        try:
            df = pd.read_json(json_path)
            
            df['customer_id'] = df['customer'].apply(lambda x: x['id'])
            df['customer_username'] = df['customer'].apply(lambda x: x['username'])
            df['product_id'] = df['product'].apply(lambda x: x['id'])
            df['product_name'] = df['product'].apply(lambda x: x['name'])
            df['sentiment_label'] = df['sentiment'].apply(lambda x: x['label'])
            df['sentiment_score'] = df['sentiment'].apply(lambda x: x['score'])
            
            df = df[['id', 'timestamp', 'text', 'customer_id', 'customer_username', 
                     'product_id', 'product_name', 'sentiment_label', 'sentiment_score', 
                     'source']]
            
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            table = pa.Table.from_pandas(df)
            pq.write_table(table, parquet_path)
            
            processed_directory = os.path.join(old_directory)
            if not os.path.exists(processed_directory):
                os.makedirs(processed_directory)
            shutil.move(json_path, os.path.join(processed_directory, json_file))
            
            print(f"JSON file '{json_file}' converted to Parquet and saved as '{parquet_file}' in '{parquet_directory}'.")
            
        except Exception as e:
            print(f"Error processing file '{json_file}': {e}")
