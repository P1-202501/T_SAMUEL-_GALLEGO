import pandas as pd

"""PARTE 1"""
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

columnas_criticas = ['Peso' ,'Talla','Glucosa','Colesterol']
df = df.dropna(subset=columnas_criticas)

# columna 'Fuma'
df['Fuma'] = df['Fuma'].str.lower().replace({
    'sí': True,'si':True, 'no':False, 
    'desconocido':False,'true':True,'false' :False
}).astype(bool)

# mes de la fecha
df['Mes'] = pd.to_datetime(df['Fecha de tamizaje'], format='%d/%m/%Y').dt.month



"""PARTE 2"""

#  IMC
df['IMC'] = df['Peso'] / (df['Talla']/100)**2

#clasific IMC
def clasifica_imc(imc) :
    if imc<18.5 :
        return 'bajo peso'
    elif 18.5<= imc< 25 :
         return 'Normal'
    elif 25<=  imc< 30:
        return'sobrepeso'
    else:
         return 'obesidad'

df['Clasificacion_IMC'] = df['IMC'].apply(clasifica_imc)

#  binaris
df['Sedentario'] = df['Actividad física (min/sem)'] < 60
df['Hipertenso'] = (df['PAS'] >= 140) | (df['PAD'] >= 90)

#alterado
condiciones= [
    (df['Glucosa']> 126 ),
    (df['Colesterol' ]> 240 ) ,
    (df['IMC']> 30 ) ,
    df['Sedentario' ]
]
df['Metabolicamente_alterado'] = sum(condiciones) >=2


"""PARTE 3"""
# agrup por región
riesgo_region = df.groupby('Región')['Metabolicamente_alterado']
region_mas_riesgosa= riesgo_region.idxmax()
print("Región con mayor riesgo metabólico:")
print(region_mas_riesgosa.idxmax())

# agrup por mes
sedentarismo_mes = df.groupby('Mes')['Sedentario']
mes_mas_sedentario= sedentarismo_mes.idxmax()
print("Meses con mayor sedentarismo:")
print(mes_mas_sedentario.idxmax())
  
"""PARTE 4"""
import matplotlib.pyplot as plt  

df['Clasificacion_IMC'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribución de la Clasificación del IMC')
plt.xlabel('Clasificación')
plt.ylabel('Número de pacientes')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
