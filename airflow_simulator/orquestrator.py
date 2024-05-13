import time
import schedule
from multiprocessing import Process

from database.database import create_database_in_memory

from pipelines.injest_database import fetch_data, save_to_parquet
from pipelines.injest_api import fetch_reviews, process_reviews
from pipelines.injest_sftp import injest_csv
from pipelines.pre_process_sftp import convert_csv_to_parquet
from pipelines.pre_process_api import convert_json_to_parquet
from pipelines.raw_database import merge_parquet_files
from pipelines.raw_api import merge_parquet_files_api
from pipelines.raw_sftp import merge_parquet_files_sftp
from pipelines.clean_database import add_metadata_columns,load_parquet_files
from pipelines.clean_sftp import add_metadata_columns_sftp,load_parquet_files_sftp
from pipelines.clean_api import add_metadata_columns_api,load_parquet_files_api


from api_sentiment_analyst import api

def task_database_ingestion():
    print("----------------------------------------------------------------------")
    print("Creating Database...")
    start_time = time.time()
    conn = create_database_in_memory()
    
    print("----------------------------------------------------------------------")
    print("Injecting Data from the Production Database...")
    df_customer, df_order, df_product, df_stock, df_store, df_store_product = fetch_data(conn)
    dataframes = {
        "customer": df_customer,
        "order_product": df_order,
        "product": df_product,
        "stock": df_stock,
        "store": df_store,
        "store_product": df_store_product
    }
    save_to_parquet(dataframes)
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"Database Ingestion Completed in {end_time - start_time:.2f} seconds.")
    conn.close()

def task_api_consumption():
    print("----------------------------------------------------------------------")
    print("Injecting Data from the Sentiment Analysis API...")
    start_time = time.time()
    reviews_data = fetch_reviews()    
    process_reviews(reviews_data)
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"API Consumption Completed in {end_time - start_time:.2f} seconds.")
    
def task_csv_consumption():
    print("----------------------------------------------------------------------")
    print("Injecting Data from the SFTP...")
    start_time = time.time()
    injest_csv()
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"CSV Consumption Completed in {end_time - start_time:.2f} seconds.")
    
def task_pre_process_csv():
    print("----------------------------------------------------------------------")
    print("Processing Data from the landing...")
    start_time = time.time()
    convert_csv_to_parquet()
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"CSV Processed in {end_time - start_time:.2f} seconds.")
    
def task_pre_process_api():
    print("----------------------------------------------------------------------")
    print("Processing Data from the landing...")
    start_time = time.time()
    convert_json_to_parquet()
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"API Processed in {end_time - start_time:.2f} seconds.")
    
def task_raw_database():
    print("----------------------------------------------------------------------")
    print("Processing Data from the pre-process...")
    start_time = time.time()
    source_dir = "datalake/pre-process/db-postgres-prod/new/"
    source_dest = "datalake/raw-data/db-postgres-prod/"
    old_dir = "datalake/pre-process/db-postgres-prod/old/"
    folder_name="customer"
    merge_parquet_files(f'{source_dir}{folder_name}',f'{source_dest}{folder_name}',f'{old_dir}{folder_name}',folder_name)
    
    folder_name="order_product"
    merge_parquet_files(f'{source_dir}{folder_name}',f'{source_dest}{folder_name}',f'{old_dir}{folder_name}',folder_name)
    
    folder_name="product"
    merge_parquet_files(f'{source_dir}{folder_name}',f'{source_dest}{folder_name}',f'{old_dir}{folder_name}',folder_name)
    
    folder_name="stock"
    merge_parquet_files(f'{source_dir}{folder_name}',f'{source_dest}{folder_name}',f'{old_dir}{folder_name}',folder_name)
    
    folder_name="store"
    merge_parquet_files(f'{source_dir}{folder_name}',f'{source_dest}{folder_name}',f'{old_dir}{folder_name}',folder_name)
    
    folder_name="store_product"
    merge_parquet_files(f'{source_dir}{folder_name}',f'{source_dest}{folder_name}',f'{old_dir}{folder_name}',folder_name)
    
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"Database Processed in {end_time - start_time:.2f} seconds.")
    
def task_raw_api():
    print("----------------------------------------------------------------------")
    print("Processing Data from the pre-process...")
    start_time = time.time()
    merge_parquet_files_api()
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"API Processed in {end_time - start_time:.2f} seconds.")
    
def task_raw_sftp():
    print("----------------------------------------------------------------------")
    print("Processing Data from the pre-process...")
    start_time = time.time()
    merge_parquet_files_sftp()
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"SFTP Processed in {end_time - start_time:.2f} seconds.")
    
def task_clean_database():
    print("----------------------------------------------------------------------")
    print("Processing Data from the raw data...")
    start_time = time.time()
    source_dir = "datalake/raw-data/db-postgres-prod/"
    source_dest = "datalake/clean-data/db-postgres-prod/"
    folder_name="customer"
    df = load_parquet_files(f'{source_dir}{folder_name}',folder_name)
    add_metadata_columns(df,f'{source_dest}{folder_name}',folder_name)
    
    folder_name="order_product"
    df = load_parquet_files(f'{source_dir}{folder_name}',folder_name)
    add_metadata_columns(df,f'{source_dest}{folder_name}',folder_name)
        
    folder_name="product"
    df = load_parquet_files(f'{source_dir}{folder_name}',folder_name)
    add_metadata_columns(df,f'{source_dest}{folder_name}',folder_name)
        
    folder_name="stock"
    df = load_parquet_files(f'{source_dir}{folder_name}',folder_name)
    add_metadata_columns(df,f'{source_dest}{folder_name}',folder_name)
        
    folder_name="store"
    df = load_parquet_files(f'{source_dir}{folder_name}',folder_name)
    add_metadata_columns(df,f'{source_dest}{folder_name}',folder_name)
        
    folder_name="store_product"
    df = load_parquet_files(f'{source_dir}{folder_name}',folder_name)
    add_metadata_columns(df,f'{source_dest}{folder_name}',folder_name)
        
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"Database Processed in {end_time - start_time:.2f} seconds.")
    
def task_clean_sftp():
    print("----------------------------------------------------------------------")
    print("Processing Data from the raw-data...")
    start_time = time.time()
    df_sftp = load_parquet_files_sftp()
    add_metadata_columns_sftp(df_sftp)
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"SFTP Processed in {end_time - start_time:.2f} seconds.")

def task_clean_api():
    print("----------------------------------------------------------------------")
    print("Processing Data from the raw-data...")
    start_time = time.time()
    df_api = load_parquet_files_api()
    add_metadata_columns_api(df_api)
    end_time = time.time()
    print("----------------------------------------------------------------------")
    print(f"API Processed in {end_time - start_time:.2f} seconds.")
    
def orchestrate():
    # Pre-Processing Database
    database_pre_process = Process(target=task_database_ingestion)
    database_pre_process.start()
    # Raw-Processing Database
    database_raw = Process(target=task_raw_database)
    database_raw.start()
    # Clean-Processing Database
    database_clean = Process(target=task_clean_database)
    database_clean.start()
    
    # API Consumption
    api_landing = Process(target=task_api_consumption)
    api_landing.start()
    # Pre-Processing API
    api_pre_process = Process(target=task_pre_process_api)
    api_pre_process.start()
    # Raw-Processing API
    api_raw = Process(target=task_raw_api)
    api_raw.start()
    # Clean-Processing SFTP
    api_clean = Process(target=task_clean_api)
    api_clean.start()
    
    # SFTP Consumption
    sftp_landing = Process(target=task_csv_consumption)
    sftp_landing.start()   
    # Pre-Processing SFTP
    sftp_pre_process = Process(target=task_pre_process_csv)
    sftp_pre_process.start()
    # Raw-Processing SFTP
    sftp_raw = Process(target=task_raw_sftp)
    sftp_raw.start()
    # Clean-Processing SFTP
    sftp_clean = Process(target=task_clean_sftp)
    sftp_clean.start()
    
    

# Schedule
schedule.every(0.5).minutes.do(task_database_ingestion)
schedule.every(0.5).minutes.do(task_api_consumption)
schedule.every(0.5).minutes.do(task_csv_consumption)
schedule.every(0.6).minutes.do(task_pre_process_csv)
schedule.every(0.6).minutes.do(task_pre_process_api)
schedule.every(0.7).minutes.do(task_raw_database)
schedule.every(0.7).minutes.do(task_raw_api)
schedule.every(0.7).minutes.do(task_raw_sftp)
schedule.every(0.8).minutes.do(task_clean_database)
schedule.every(0.8).minutes.do(task_clean_sftp)
schedule.every(0.8).minutes.do(task_clean_api)


while True:
    schedule.run_pending()
    time.sleep(1)