import pandas as pd

#--------------------------------------------------- Funciones ------------------------------------------------------------#

def create_dataframe_sql(conn, data, data_name):
    dataframe = pd.DataFrame(data)
    try:
        dataframe.to_sql(data_name,conn, index=False, if_exists='replace')
        return print(f'Dataframe "{data_name}" creada exitosamente.')
    except Exception as e:
        print(F'Error creando la dataframe: {e}.')

# ----------------------------------------------------------------------------------------------------------------------- #

def excecute_query(query,connection):
    result = pd.read_sql(query,connection)
    return print(result)

# ----------------------------------------------------------------------------------------------------------------------- #