import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('titanic.csv')

# Rellenar los valores faltantes en la columna "Age" con el valor medio de la columna
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Crear una nueva figura para la distribución de edades usando matplotlib
plt.figure()
plt.title('Histograma de la distribución de edades en el Titanic (matplotlib)')
df['Age'].plot.hist()

# Crear una nueva figura para la distribución de edades usando seaborn
plt.figure()
plt.title('Histograma de la distribución de edades en el Titanic (seaborn)')
sns.histplot(data=df, x='Age')

# Crear una nueva figura para la relación entre la edad y la tarifa pagada por el pasaje usando matplotlib
plt.figure()
plt.title('Relación entre la edad y la tarifa pagada por el pasaje (matplotlib)')
plt.scatter(df['Age'], df['Fare'])

# Crear una nueva figura para la relación entre la edad y la tarifa pagada por el pasaje usando seaborn
plt.figure()
plt.title('Relación entre la edad y la tarifa pagada por el pasaje (seaborn)')
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived')

# Crear una nueva figura para el gráfico de línea de la columna "Age" usando matplotlib
plt.figure()
plt.title('Gráfico de línea de la columna "Age" (matplotlib)')
df['Age'].plot.line()

# Crear una nueva figura para el gráfico de línea de la columna "Age" usando seaborn
plt.figure()
plt.title('Gráfico de línea de la columna "Age" (seaborn)')
sns.lineplot(data=df, x=df.index, y='Age')

# Crear una nueva figura para la supervivencia por género usando matplotlib
plt.figure()
plt.title('Supervivencia por género (matplotlib)')
df.groupby(['Sex', 'Survived']).size().unstack().plot.bar()

# Crear una nueva figura para la supervivencia por género usando seaborn
plt.figure()
plt.title('Supervivencia por género (seaborn)')
sns.countplot(data=df, x='Sex', hue='Survived')

# Crear una nueva figura para la supervivencia por clase usando matplotlib
plt.figure()
plt.title('Supervivencia por clase de pasajero (matplotlib)')
df.groupby(['Pclass', 'Survived']).size().unstack().plot.bar()

# Crear una nueva figura para la supervivencia por clase usando seaborn
plt.figure()
plt.title('Supervivencia por clase de pasajero (seaborn)')
sns.countplot(data=df, x='Pclass', hue='Survived')

# Mostrar todas las figuras
plt.show()
