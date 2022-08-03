def dropear_columnas_object(df):
    for i in df:
        if df[i].dtype == 'object':
            df.drop(columns=i,inplace=True)
   
    
def llenar_nulos_promedio(df):
    for i in df:
        df[i].fillna(df[i].mean(),inplace=True)