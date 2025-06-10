import pandas as pd
import sqlite3
import funciones.test_func as tf

conn = sqlite3.connect('mi_base.db') 
tables = tf.excecute_query_tables(conn)

dfs = tf.create_df_variable(tables, conn)
transactions = dfs['transactions']
customers= dfs['customers']
products = dfs['products']

"""
Problem Statement
Find the top 2 customers who spent the most money (net total amount) on transactions, considering only successful credit transactions.

Requirements:
Use only credit transactions.

Use either SQL or pandas (your choice).

Return a table (or DataFrame) with:

- customer_id
- customer_name
- total_credit_amount

Sort from highest to lowest.
Show only the top 2.
"""

query_1 = """
#SELECT * 
#FROM transactions 
#WHERE customer_id = '101'
#"""

#tf.excecute_query(query_1,conn)