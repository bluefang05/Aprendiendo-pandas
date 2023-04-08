import pandas as pd
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
df = pd.read_csv('SP500_data.csv')

# Convertir la columna "Date" a datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extraer el año de la columna "Date"
df['Year'] = df['Date'].dt.year

# Calcular estadísticas descriptivas
print(df.describe())

# Filtrar datos de un rango específico de años
start_year = 2000
end_year = 2020
filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

# Calcular el promedio anual de la columna "SP500"
average_yearly_SP500 = filtered_df.groupby('Year')['SP500'].mean()

# Mostrar el promedio anual de la columna "SP500"
print(average_yearly_SP500)

# Visualizar la evolución del SP500 a lo largo del tiempo
plt.plot(filtered_df['Date'], filtered_df['SP500'])
plt.xlabel('Date')
plt.ylabel('SP500')
plt.title('Evolución del SP500 (2000-2020)')
plt.show()

# Visualizar la relación entre el SP500 y la tasa de interés a largo plazo
plt.scatter(filtered_df['SP500'], filtered_df['Long Interest Rate'])
plt.xlabel('SP500')
plt.ylabel('Long Interest Rate')
plt.title('Relación entre el SP500 y la tasa de interés a largo plazo (2000-2020)')
plt.show()
