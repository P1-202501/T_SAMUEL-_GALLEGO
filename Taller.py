import pandas as pd

# 1. Cargar el archivo y mostrar primeras filas
df = pd.read_csv('biometria_pacientes.csv', sep=';', encoding='latin-1')


#2. Identificar duplicados, nulos y valores únicos
# Dupli
print(f"Número de duplicados:{df.duplicated().sum()}")

# Nulos por colum
print(df.isnull().sum())
# Valores únicos en 'Fuma'
print(df['Fuma'].unique())
