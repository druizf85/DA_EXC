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
Challenge #2: Monthly revenue trend for the store
Problem Statement:
Calculate the total net revenue per month from all transactions.
Only include credit transactions.

Requirements:
Output should include:

month (e.g., '2023-01')

total_credit_amount

Sort by month in ascending order.

Use either SQL or pandas.

🔧 Optional: If you're using pandas, format transaction_date properly if it's not already a datetime.

Let me know when you're ready — and I’ll challenge you with something involving the products table next!
"""

#SQL 


#Python