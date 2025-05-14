import pandas as pd

# 1. Cargar el archivo y mostrar primeras filas
df = pd.read_csv('biometria_pacientes.csv', sep=';', encoding='latin-1')


#2. identificar duplicados, nulos y valores únicos
# Dupli
print(f"Número de duplicados:{df.duplicated().sum()}")

# nulos por colum
print(df.isnull().sum())
# Valores únicos en 'Fuma'
print(df['Fuma'].unique())


# 3. eliminar duplicados por columnas criticas
df = df.drop_duplicates()

columnas_criticas = ['Peso', 'Talla', 'Glucosa', 'Colesterol']
df = df.dropna(subset=columnas_criticas)

# columna 'Fuma'
df['Fuma'] = df['Fuma'].str.lower().replace({
    'sí': True, 'si': True, 'no': False, 
    'desconocido': False, 'true': True, 'false': False
}).astype(bool)

# mes de la fecha
df['Mes'] = pd.to_datetime(df['Fecha de tamizaje'], format='%d/%m/%Y').dt.month

print(df)