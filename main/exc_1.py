import pandas as pd
import sqlite3
import funciones.test_func as tf

conn = sqlite3.connect('mi_base.db') 
tables = tf.excecute_query_tables(conn)

dfs = tf.create_df_variable(tables, conn)
transactions = dfs['transactions']
customers= dfs['customers']
products = dfs['products']
 
#query_1 = """
#SELECT * 
#FROM transactions 
#WHERE customer_id = '101'
#"""

#tf.excecute_query(query_1,conn)