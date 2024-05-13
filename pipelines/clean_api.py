import os
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
from datetime import datetime

def add_metadata_columns_api(df):
    destination_directory = "datalake/clean-data/api-sentiment-analyze"
    folder_name = "reviews"
    os.makedirs(destination_directory, exist_ok=True)
    
    df['load_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['source'] = f"api_analyze_sentiment/{folder_name}"

    file_path = os.path.join(destination_directory, f"{folder_name}_clean.parquet")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)
    
    print(f"Clean data saved in '{destination_directory}'.")

def load_parquet_files_api():
    source_directory =  "datalake/raw-data/api-sentiment-analyze"
    folder_name = "reviews"
    
    parquet_path = os.path.join(source_directory, f"{folder_name}.parquet")
    if not os.path.exists(parquet_path):
        print(f"No Parquet file found in the directory '{source_directory}'.")
        return None
    
    table = pq.read_table(parquet_path)
    df = table.to_pandas()
    return df
