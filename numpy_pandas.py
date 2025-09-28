"""
Script: pandas_numpy_demo.py
Autor: Sergio
Descripción:
    Este script muestra un ejemplo práctico y sencillo del uso de las librerías
    NumPy y Pandas en Python, pensado para personas que están aprendiendo a programar.
    
    Se utilizan las siguientes funcionalidades:
    - Crear un array de NumPy con datos numéricos.
    - Realizar operaciones matemáticas básicas sobre el array.
    - Crear un DataFrame de Pandas a partir de un diccionario de datos.
    - Calcular estadísticas descriptivas con Pandas.
    - Filtrar y seleccionar datos en el DataFrame.
    
    Librerías:
        - numpy: Para trabajar con arrays numéricos y operaciones matemáticas.
        - pandas: Para manipular y analizar datos en forma tabular (filas y columnas).
    
    Ejemplo de salida:
        Array de NumPy:
         [10 20 30 40 50]
        
        Array multiplicado por 2:
         [ 20  40  60  80 100]
        
        DataFrame de Pandas:
             Nombre  Edad   Ciudad
        0     Ana    23   Madrid
        1    Luis    30  Barcelona
        2   Marta    27   Valencia
        3  Alberto    35   Sevilla
        
        Estadísticas de las edades:
        count     4.000000
        mean     28.750000
        std       5.123475
        min      23.000000
        25%      25.000000
        50%      28.500000
        75%      32.250000
        max      35.000000
        Name: Edad, dtype: float64
"""

import numpy as np
import pandas as pd


def ejemplo_numpy():
    """Ejemplo básico con NumPy."""
    # Crear un array de NumPy con números enteros
    numeros = np.array([10, 20, 30, 40, 50])
    print("Array de NumPy:\n", numeros)

    # Operación: multiplicar todos los elementos por 2
    multiplicado = numeros * 2
    print("\nArray multiplicado por 2:\n", multiplicado)


def ejemplo_pandas():
    """Ejemplo básico con Pandas."""
    # Crear un DataFrame a partir de un diccionario
    datos = {
        "Nombre": ["Ana", "Luis", "Marta", "Alberto"],
        "Edad": [23, 30, 27, 35],
        "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla"]
    }

    df = pd.DataFrame(datos)
    print("\nDataFrame de Pandas:\n", df)

    # Calcular estadísticas de la columna Edad
    print("\nEstadísticas de las edades:")
    print(df["Edad"].describe())

    # Filtrar personas mayores de 25 años
    print("\nPersonas mayores de 25 años:")
    print(df[df["Edad"] > 25])


if __name__ == "__main__":
    print("=== Ejemplo con NumPy ===")
    ejemplo_numpy()

    print("\n=== Ejemplo con Pandas ===")
    ejemplo_pandas()
