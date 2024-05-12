import sqlite3
import pandas as pd

def fetch_data(conn):
    query_customer = "SELECT * FROM customer"
    query_order = "SELECT * FROM order_product"
    query_product = "SELECT * FROM product"
    query_stock = "SELECT * FROM stock"
    query_store = "SELECT * FROM store"
    query_store_product = "SELECT * FROM store_product"

    df_customer = pd.read_sql_query(query_customer, conn)
    df_order = pd.read_sql_query(query_order, conn)
    df_product = pd.read_sql_query(query_product, conn)
    df_stock = pd.read_sql_query(query_stock, conn)
    df_store = pd.read_sql_query(query_store, conn)
    df_store_product = pd.read_sql_query(query_store_product, conn)

    return df_customer, df_order, df_product, df_stock, df_store, df_store_product

def save_to_parquet(dataframes):
    for name, df in dataframes.items():
        df.to_parquet(f"datalake/pre-process/db-postgres-prod/new/{name}.parquet")