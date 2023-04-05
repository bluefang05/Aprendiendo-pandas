import pandas as pd

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('titanic.csv')

# Filtrar las filas donde la columna "Age" es mayor que 30 y la columna "Sex" es "female"
advanced_filter = df[(df['Age'] > 30) & (df['Sex'] == 'female')]

# Mostrar las primeras 5 filas del DataFrame filtrado
print('\nPrimeras 5 filas del DataFrame filtrado:')
print('-----------------------------------------')
print(advanced_filter.head())

# Establecer la columna "Name" como índice
df = df.set_index('Name')

# Reiniciar el índice para que sea numérico
df = df.reset_index(drop=True)

# Agrupar los datos por la columna "Sex" y calcular la media de la columna "Age" en cada grupo
avg_age_by_sex = df.groupby('Sex')['Age'].mean()

# Mostrar la media de edad para cada género
print('\nMedia de edad para cada género:')
print('--------------------------------')
print(avg_age_by_sex)

# Crear un nuevo DataFrame con información adicional sobre los pasajeros
additional_info = pd.DataFrame({
    'Name': ['John Smith', 'Jane Doe'],
    'Occupation': ['Engineer', 'Doctor']
})

# Leer de nuevo el archivo CSV para obtener el DataFrame con la columna "Name" original
df = pd.read_csv('titanic.csv')

# Unir el DataFrame original con el DataFrame de información adicional en la columna "Name"
merged_df = pd.merge(df, additional_info, on='Name')

# Mostrar las primeras 5 filas del DataFrame combinado
print('\nPrimeras 5 filas del DataFrame combinado:')
print('------------------------------------------')
print(merged_df.head())


# Este código realiza las siguientes acciones:

#     Importa la biblioteca pandas.
#     Lee el archivo 'titanic.csv' y lo convierte en un DataFrame.
#     Filtra las filas donde la columna 'Age' es mayor que 30 y la columna 'Sex' es 'female' y muestra las primeras 5 filas del DataFrame filtrado.
#     Establece la columna 'Name' como índice y luego reinicia el índice para que sea numérico.
#     Agrupa los datos por la columna 'Sex' y calcula la media de la columna 'Age' en cada grupo, mostrando la media de edad para cada género.
#     Crea un nuevo DataFrame con información adicional sobre los pasajeros y vuelve a leer el archivo CSV para obtener el DataFrame con la columna 'Name' original.
#     Une el DataFrame original con el DataFrame de información adicional en la columna 'Name' y muestra las primeras 5 filas del DataFrame combinado.
