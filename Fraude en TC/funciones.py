#Elimina las columnas de un dataframe que sean object
def dropear_columnas_object(df):
    for i in df:
        if df[i].dtype == 'object':
            df.drop(columns=i,inplace=True)
   
#Reemplaza los valores nulos por el promedio de la columna
def llenar_nulos_promedio(df):
    for i in df:
        df[i].fillna(df[i].mean(),inplace=True)