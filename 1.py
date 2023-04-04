import pandas as pd

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('titanic.csv')

# Mostrar las primeras 5 filas del DataFrame
print('Mostrar las primeras 5 filas del DataFrame')
print(df.head())

# Seleccionar la columna "Age" del DataFrame
print('Seleccionar la columna "Age" del DataFrame')
ages = df['Age']

# Mostrar las primeras 5 edades en la columna "Age"
print('Mostrar las primeras 5 edades en la columna "Age"')
print(ages.head())
