import pandas as pd

df = pd.read_csv('titanic.csv')

# Seleccionar la fila con índice 3 utilizando el método loc
print('\nSeleccionar la fila con índice 3 utilizando el método loc:')
print('-------------------------------------------------------------')
row = df.loc[3]
print(row)

# Seleccionar la primera columna utilizando corchetes
print('\nSeleccionar la primera columna utilizando corchetes:')
print('----------------------------------------------------')
first_column = df['Survived']
print(first_column)

# Seleccionar las filas 0 a 4 y las columnas "Name" y "Age" utilizando loc
print('\nSeleccionar las filas 0 a 4 y las columnas "Name" y "Age" utilizando loc:')
print('--------------------------------------------------------------------------')
subset = df.loc[0:4, ['Name', 'Age']]
print(subset)

# Ordenar el DataFrame por la columna "Age" en orden descendente
sorted_df = df.sort_values('Age', ascending=False)

# Mostrar las primeras 5 filas del DataFrame ordenado
print('\nMostrar las primeras 5 filas del DataFrame ordenado:')
print('-----------------------------------------------------')
print(sorted_df.head())

# Agregar una nueva columna con el número de familiares a bordo
df['Family Size'] = df['SibSp'] + df['Parch']

# Eliminar la columna "Embarked"
df = df.drop('Embarked', axis=1)


# Este código realiza las siguientes acciones:

#     Importa la biblioteca pandas.
#     Lee el archivo 'titanic.csv' y lo convierte en un DataFrame.
#     Selecciona la fila con índice 3 utilizando el método loc y la muestra en pantalla.
#     Selecciona la columna 'Survived' y la muestra en pantalla.
#     Selecciona las filas 0 a 4 y las columnas 'Name' y 'Age' utilizando loc y muestra el resultado en pantalla.
#     Ordena el DataFrame por la columna 'Age' en orden descendente y muestra las primeras 5 filas.
#     Agrega una nueva columna llamada 'Family Size' que representa el número de familiares a bordo.
#     Elimina la columna 'Embarked' del DataFrame.