import time
import schedule
from multiprocessing import Process

from pipeline_injest.injest_database import fetch_data, save_to_parquet
from database.database import create_database_in_memory, get_table_info
from pipeline_injest.injest_api import fetch_reviews, process_reviews
from pipeline_injest.injest_sftp import injest_csv
from pipeline_injest.pre_process_sftp import convert_csv_to_parquet
from pipeline_injest.pre_process_api import convert_json_to_parquet
from api_sentiment_analyst import api

def task_database_ingestion():
    print("----------------------------------------------------------------------")
    print("Creating Database...")
    start_time = time.time()
    conn = create_database_in_memory()
    # get_table_info(conn)
    
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

def orchestrate():
    # Database Ingestion
    database_pre_process = Process(target=task_database_ingestion)
    database_pre_process.start()
    
    # API Consumption
    api_landing = Process(target=task_api_consumption)
    api_landing.start()
    # Pre-Processing API
    api_pre_process = Process(target=task_pre_process_api)
    api_pre_process.start()
    
    # SFTP Consumption
    sftp_landing = Process(target=task_csv_consumption)
    sftp_landing.start()   
    # Pre-Processing CSV
    sftp_pre_process = Process(target=task_pre_process_csv)
    sftp_pre_process.start()

# Schedule
schedule.every(0.3).minutes.do(task_database_ingestion)
schedule.every(0.3).minutes.do(task_api_consumption)
schedule.every(0.3).minutes.do(task_csv_consumption)
schedule.every(0.4).minutes.do(task_pre_process_csv)
schedule.every(0.4).minutes.do(task_pre_process_api)


while True:
    schedule.run_pending()
    time.sleep(1)