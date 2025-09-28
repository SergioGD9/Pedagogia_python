"""
Script: fibonacci.py
Autor: Sergio
Descripción:
    Este script genera la secuencia de Fibonacci hasta un número dado de términos.
    
    La secuencia de Fibonacci es una serie matemática donde:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2)  (para n > 1)
    
    Ejemplo:
        Entrada: 10
        Salida: 0 1 1 2 3 5 8 13 21 34
"""

def fibonacci(n: int) -> list:
    """
    Genera la secuencia de Fibonacci hasta n términos.
    
    Parámetros:
        n (int): Número de términos a generar. Debe ser mayor que 0.
    
    Retorna:
        list: Lista con los n primeros números de la secuencia de Fibonacci.
    
    Ejemplo:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n <= 0:
        raise ValueError("El número de términos debe ser mayor que 0.")
    
    secuencia = [0, 1]
    
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    
    return secuencia[:n]


if __name__ == "__main__":
    # Pedimos al usuario cuántos términos quiere generar
    try:
        n = int(input("¿Cuántos términos de la secuencia de Fibonacci quieres generar? "))
        print(f"Secuencia de Fibonacci con {n} términos:")
        print(fibonacci(n))
    except ValueError as e:
        print(f"Error: {e}")
