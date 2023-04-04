import pandas as pd

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('titanic.csv')

# Mostrar las primeras 5 filas del DataFrame
print('\nMostrar las primeras 5 filas del DataFrame:')
print('---------------------------------------------')
print(df.head())

# Seleccionar la columna "Age" del DataFrame
ages = df['Age']

# Mostrar las primeras 5 edades en la columna "Age"
print('\nMostrar las primeras 5 edades en la columna "Age":')
print('----------------------------------------------------')
print(ages.head())

# Filtrar solo las filas donde la columna "Sex" es igual a "female"
female_passengers = df[df['Sex'] == 'female']

# Mostrar las primeras 5 filas de mujeres en el DataFrame
print('\nMostrar las primeras 5 filas de mujeres en el DataFrame:')
print('-----------------------------------------------------------')
print(female_passengers.head())

# Agrupar los datos por la columna "Pclass" y calcular la media de la columna "Fare" en cada grupo
avg_fares_by_class = df.groupby('Pclass')['Fare'].mean()

# Mostrar la media de la tarifa de cada clase de pasajero
print('\nMostrar la media de la tarifa de cada clase de pasajero:')
print('----------------------------------------------------------')
print(avg_fares_by_class)


# Este código realiza las siguientes acciones:

#     Importa la biblioteca pandas.
#     Lee el archivo 'titanic.csv' y lo convierte en un DataFrame.
#     Muestra las primeras 5 filas del DataFrame.
#     Selecciona la columna 'Age' y muestra las primeras 5 edades.
#     Filtra las filas donde la columna 'Sex' es igual a 'female' y muestra las primeras 5 filas de mujeres.
#     Agrupa los datos por la columna 'Pclass' y calcula la media de la columna 'Fare' en cada grupo.
#     Muestra la media de la tarifa de cada clase de pasajero.