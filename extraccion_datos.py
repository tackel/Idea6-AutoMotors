import pandas as pd
from pathlib import Path

path = Path(__file__).parent



def read_ventas():
    df_ventas = pd.read_csv(f'{path}/Ventas.csv', sep=';', low_memory=False)


def normalizacion_empleados():
    df_empleados = pd.read_csv(f'{path}/Empleados.csv', sep=';')
    print(df_empleados.head())
    #print(df_empleados.info())
    #print(df_empleados.describe())
    print(df_empleados.dtypes)
    #print(df_empleados.isna())
    #print(df_empleados.drop_duplicates())
    #print(df_empleados.iloc[:,1])
    #print(df_empleados.value_counts())
    print('Data set Empleados no requiere cambios')

def normalizacion_ventas():
    
    df_ventas = pd.read_csv(f'{path}/Ventas.csv', sep=';', low_memory=False)
    #print(df_ventas.info())
    df_ventas2 = df_ventas.drop_duplicates()
    #print(df_ventas2)
    #print(df_ventas2.isna())
    df_ventas2 = df_ventas2.drop(index=[127265, 127255])
    #print(df_ventas2.dtypes)
    #print(df_ventas2.Cantidad == '1,006')
    print('------')
    df_ventas2['Empleado'] = pd.to_numeric(df_ventas2.Empleado, errors= 'raise')
    df_ventas2.Fecha = pd.to_datetime(df_ventas2['Fecha'], format='%d/%m/%Y')
    
    df_ventas2['Cantidad'] = pd.to_numeric(df_ventas2['Cantidad'], errors='coerce')
    print(df_ventas2.iloc[107700:107705,8].isna())

    #df_ventas2.Ventas = df_ventas2['Ventas'].astype(float, errors= 'raise')
    print(df_ventas2.head())
    #print(df_ventas2[['Fecha','CodigoFamilia','Familia','Cantidad','Ventas']])
    print(df_ventas2.dtypes)
  
  


#normalizacion_empleados()
normalizacion_ventas()