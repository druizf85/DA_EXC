import sqlite3
import pandas as pd
import funciones.test_func as tf

data_transactions = {
    'transaction_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_id': [101, 102, 101, 103, 102, 101, 104, 103, 102, 101],
    'transaction_date': [
        '2023-01-05', '2023-01-07', '2023-01-15', '2023-01-20', '2023-02-02',
        '2023-02-14', '2023-02-18', '2023-03-01', '2023-03-02', '2023-03-10'
    ],
    'amount': [200, -100, 500, 1200, -50, -300, 400, -200, 1000, -100],
    'type': ['credit', 'debit', 'credit', 'credit', 'debit', 'debit', 'credit', 'debit', 'credit', 'debit']
}

data_name_trans='transactions'
conn= sqlite3.connect(':memory:') 

tf.create_dataframe_sql(conn, data_transactions, data_name_trans)

query_1= """
SELECT * 
FROM transactions 
WHERE customer_id = '101'
"""

tf.excecute_query(query_1,conn)