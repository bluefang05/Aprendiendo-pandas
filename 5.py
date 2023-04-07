import pandas as pd

# Leer el archivo CSV y convertirlo en un DataFrame
df = pd.read_csv('SP500_data.csv')

# Convertir la columna "Date" a datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extraer el año de la columna "Date"
df['Year'] = df['Date'].dt.year

# Agrupar los datos por año y calcular la media de la columna "Price"
avg_price_by_year = df.groupby('Year')['Price'].mean()

# Mostrar el precio promedio por año
print(avg_price_by_year)
