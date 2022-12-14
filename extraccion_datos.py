import pandas as pd
from pathlib import Path

path = Path(__file__).parent

def normalizacion_empleados():
    df_empleados = pd.read_csv(f'{path}/Empleados.csv', sep=';')
   
    #print(df_empleados.info())
    #print(df_empleados.describe())
    
    #print(df_empleados.isna())
    #print(df_empleados.drop_duplicates())
    #print(df_empleados.iloc[:,1])
    #print(df_empleados.value_counts())
    print('Data set Empleados no requiere cambios')

def normalizacion_ventas():
    # Obtener loa datos del archivo csv
    df_ventas = pd.read_csv(f'{path}/Ventas.csv', sep=';', low_memory=False)
    #print(df_ventas.info())
    # Eliminar registros duplicados
    df_ventas = df_ventas.drop_duplicates()
    # Eliminar registros nan
    df_ventas = df_ventas.dropna()

    # pasar columna empleados a numerico
    df_ventas['Empleado'] = df_ventas['Empleado'].astype('int', errors= 'raise')
    # pasar columna fecha a formato fecha
    df_ventas.Fecha = pd.to_datetime(df_ventas['Fecha'], format='%d/%m/%Y')
    #pasar columna candad a numerico
    df_ventas['Cantidad'] = pd.to_numeric(df_ventas['Cantidad'], errors='coerce')
    # obtengo la media para cambiar los nan
    mean_df = df_ventas['Cantidad'].mean()
    # Cambio nan por el valor medio
    df_ventas.fillna(mean_df, inplace=True)
    # Cambio columna canidad a entero
    df_ventas['Cantidad'] = df_ventas['Cantidad'].astype('int', errors= 'raise')

    # Pasar columna Ventas a float
    # filtrar comillas y comas de la columna ventas.
    
    df_ventas['Ventas'] = df_ventas['Ventas'].apply(lambda x : x.split(',')[0])
    df_ventas.Ventas = df_ventas['Ventas'].apply(lambda x : x.replace(".",""))
    # Lugo  pasar columna ventas a entero
    print(df_ventas.Ventas)
    df_ventas['Ventas'] = pd.to_numeric(df_ventas['Ventas'], errors='raise')

    # Combierto la columna ventas a dolares al cambio 0.00023
    df_ventas['Ventas_dolar'] =  round(df_ventas['Ventas'] * 0.00023,2)
    df_ventas.Ventas_dolar = df_ventas['Ventas_dolar'].apply(lambda x : str(x).replace(".",","))
   
    #df_ventas2['Cantidad'] = pd.to_numeric(df_ventas2['Cantidad'], errors='coerce')
    #print(df_ventas2.iloc[107700:107705,8].isna())
    print(df_ventas.info())
    df_ventas.to_csv(f'{path}/ventas_limpio.csv',sep=';')
  
  


normalizacion_empleados()
normalizacion_ventas()