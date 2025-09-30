import pandas as pd  # Importa la librería pandas para análisis de datos


# Cargar el archivo CSV con  este comando de kripto
datos = pd.read_csv("sentetik_kripto_veriseti_saatlik_2025.csv")


# describe() proporciona estadísticas descriptivas que resumen la tendencia central,
# la dispersión y la forma de la distribución de un conjunto de datos.
print(datos.describe())


#tipo de cada columna
print(datos.dtypes)

#Mostrar los primeros registros
print(datos.head())

#Mostrar los ultimos registros
print(datos.tail())

#calcular la media de la columna en este caso open
media_open = datos["open"].mean()
print(f"Media de la columna open: {media_open}")
#calcular la mediana de la columna en este caso opem
mediana_open = datos["open"].median()
print(f"Mediana de la columna open: {mediana_open}")
#Calcular la desiviación estandar de la columna en este caso open
desviacion_open = datos["open"].std()
print(f"Desviación de la columana open: {desviacion_open}")


