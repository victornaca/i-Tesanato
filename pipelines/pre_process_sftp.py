import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import shutil
from datetime import datetime

def convert_csv_to_parquet():
    csv_directory = "datalake/landing/csv-price-search/new"
    parquet_directory = "datalake/pre-process/csv-price-search/new"
    old_directory = "datalake/landing/csv-price-search/old"
    
    if not os.path.exists(csv_directory):
        print(f"The source directory '{csv_directory}' does not exist.")
        return
    
    if not os.path.exists(parquet_directory):
        os.makedirs(parquet_directory)
    
    csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]
    
    if not csv_files:
        print(f"No CSV files found in the directory '{csv_directory}'.")
        return
    
    for csv_file in csv_files:
        csv_path = os.path.join(csv_directory, csv_file)
        parquet_file = os.path.splitext(csv_file)[0] + ".parquet"
        parquet_path = os.path.join(parquet_directory, parquet_file)
        
        df = pd.read_csv(csv_path)
        
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_path)
        
        print(f"CSV file '{csv_file}' converted to Parquet and saved as '{parquet_file}' in '{parquet_directory}'.")
        
        processed_directory = os.path.join(old_directory)
        if not os.path.exists(processed_directory):
            os.makedirs(processed_directory)
        shutil.move(csv_path, os.path.join(processed_directory, csv_file))