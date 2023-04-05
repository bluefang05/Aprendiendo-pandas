import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('titanic.csv')

# Identificar filas con datos faltantes en la columna "Age"
null_age = df[df['Age'].isnull()]

# Rellenar los valores faltantes en la columna "Age" con el valor medio de la columna
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

print('\nEdades del DataFrame después de rellenar los valores faltantes:')
print('----------------------------------------------------------------')
print(df['Age'])

# Crear una nueva figura para la distribución de edades
plt.figure()
plt.title('Distribución de edades en el conjunto de datos')
df['Age'].plot.hist()

# Crear una nueva figura para la relación entre la edad y la tarifa pagada por el pasaje
plt.figure()
plt.title('Relación entre la edad y la tarifa pagada por el pasaje')
df.plot.scatter(x='Age', y='Fare')

# Crear una nueva figura para el gráfico de línea de la columna "Age"
plt.figure()
plt.title('Gráfico de línea de la columna "Age"')
df['Age'].plot.line()

# Mostrar todas las figuras
plt.show()

# Este código realiza las siguientes acciones:

#     Importa las bibliotecas pandas y matplotlib.pyplot.
#     Lee el archivo 'titanic.csv' y lo convierte en un DataFrame.
#     Identifica filas con datos faltantes en la columna 'Age' y rellena los valores faltantes con el valor medio de la columna.
#     Muestra las edades del DataFrame después de rellenar los valores faltantes.
#     Crea una nueva figura y grafica la distribución de edades en el conjunto de datos.
#     Crea una nueva figura y grafica la relación entre la edad y la tarifa pagada por el pasaje.
#     Crea una nueva figura y grafica la columna 'Age' como un gráfico de línea.
#     Muestra todas las figuras.