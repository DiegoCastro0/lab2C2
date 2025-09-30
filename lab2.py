import pandas as pd  # Importa la librería pandas para análisis de datos


# Cargar el archivo CSV con  este comando de kripto
datos = pd.read_csv("sentetik_kripto_veriseti_saatlik_2025.csv")


# describe() proporciona estadísticas descriptivas que resumen la tendencia central,
# la dispersión y la forma de la distribución de un conjunto de datos.
print(datos.describe())


#tipo de cada columna
print(datos.dtypes)