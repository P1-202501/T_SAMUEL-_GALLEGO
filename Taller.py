import pandas as pd

# 1. Cargar el archivo y mostrar primeras filas
df = pd.read_csv('biometria_pacientes.csv',  encoding='latin-1')
print(df)