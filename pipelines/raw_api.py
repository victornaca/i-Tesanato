import os
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
import shutil

def merge_parquet_files_api():
    source_directory = "datalake/pre-process/api-sentiment-analyze/new"
    destination_directory = "datalake/raw-data/api-sentiment-analyze"
    old_directory = "datalake/pre-process/api-sentiment-analyze/old"
    folder_name = "reviews"

    os.makedirs(destination_directory, exist_ok=True)

    parquet_files = [f for f in os.listdir(source_directory) if f.endswith('.parquet')]

    if not parquet_files:
        print(f"No Parquet files found in the directory '{source_directory}'.")
        return

    dfs = []

    for file in parquet_files:
        file_path = os.path.join(source_directory, file)
        table = pq.read_table(file_path)
        df = table.to_pandas()
        dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)

    if folder_name:
        merged_parquet_path = os.path.join(destination_directory, folder_name + '.parquet')

    table = pa.Table.from_pandas(merged_df)
    pq.write_table(table, merged_parquet_path)

    print(f"Parquet files merged and saved as '{os.path.basename(merged_parquet_path)}' in '{destination_directory}'.")

    for file in parquet_files:
        source_path = os.path.join(source_directory, file)
        destination_path = os.path.join(old_directory, file)
        shutil.move(source_path, destination_path)
    print(f"Processed Parquet files moved to '{old_directory}'.")