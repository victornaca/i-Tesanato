import os
import pyarrow.parquet as pq
import pandas as pd
import pyarrow as pa
from datetime import datetime

def add_metadata_columns(df, destination_directory, folder_name):
    os.makedirs(destination_directory, exist_ok=True)
    
    # Adiciona colunas de metadados
    df['load_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['source'] = f"db_prod_itesanato/{folder_name}"

    # Salva os dados limpos como um arquivo Parquet
    file_path = os.path.join(destination_directory, f"{folder_name}_clean.parquet")
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)
    
    print(f"Clean data saved for 'customer' in '{destination_directory}'.")

def load_parquet_files(source_directory, folder_name):
    # Carrega o arquivo Parquet do cliente
    parquet_path = os.path.join(source_directory, f"{folder_name}.parquet")
    if not os.path.exists(parquet_path):
        print(f"No Parquet file found for 'customer' in the directory '{source_directory}'.")
        return None
    
    # Lê o arquivo Parquet e retorna o DataFrame correspondente
    table = pq.read_table(parquet_path)
    df = table.to_pandas()
    return df
