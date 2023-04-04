import pandas as pd

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('titanic.csv')

# Mostrar las primeras 5 filas del DataFrame
print(' \n \n - \nMostrar las primeras 5 filas del DataFrame')
print(df.head())

# Seleccionar la columna "Age" del DataFrame
print(' \n \n - \nSeleccionar la columna "Age" del DataFrame')
ages = df['Age']

# Mostrar las primeras 5 edades en la columna "Age"
print(' \n \n - \nMostrar las primeras 5 edades en la columna "Age"')
print(ages.head())

# Filtrar solo las filas donde la columna "Sex" es igual a "female"
print(' \n \n - \nFiltrar solo las filas donde la columna "Sex" es igual a "female"')
female_passengers = df[df['Sex'] == 'female']

# Mostrar las primeras 5 filas de mujeres en el DataFrame
print(' \n \n - \nMostrar las primeras 5 filas de mujeres en el DataFrame')
print(female_passengers.head())

# Agrupar los datos por la columna "Pclass" y calcular la media de la columna "Fare" en cada grupo
print(' \n \n - \nAgrupar los datos por la columna "Pclass" y calcular la media de la columna "Fare" en cada grupo') 
avg_fares_by_class = df.groupby('Pclass')['Fare'].mean()

# Mostrar la media de la tarifa de cada clase de pasajero
print(' \n \n - \nMostrar la media de la tarifa de cada clase de pasajero')
print(avg_fares_by_class)
