def retirar_dinero(saldo, cantidad):
    """
    Función que simula la retirada de dinero de un cajero automático.
    
    Parámetros:
    saldo (float): Dinero disponible en la cuenta.
    cantidad (float): Dinero que el usuario quiere retirar.
    
    Returns:
    float: Nuevo saldo si la operación es válida.
    
    Excepciones controladas:
    - ValueError: si la cantidad no es positiva.
    - ZeroDivisionError: no aplica aquí, pero ejemplo de cómo se capturaría.
    - Exception: captura cualquier otro error inesperado.
    """
    try:
        # Lanzamos una excepción manual si la cantidad es negativa
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        # Comprobamos si hay suficiente saldo
        if cantidad > saldo:
            raise Exception("Fondos insuficientes")

        nuevo_saldo = saldo - cantidad
        print(f"Has retirado {cantidad} €. Nuevo saldo: {nuevo_saldo} €")
        return nuevo_saldo

    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Gracias por usar el cajero 😊")  # Esto se ejecuta siempre


# --- Ejecución ---
saldo = 100

print("\n✅ Caso correcto:")
saldo = retirar_dinero(saldo, 50)  # Retira 50

print("\n❌ Retiro de cantidad negativa:")
saldo = retirar_dinero(saldo, -20) # Error controlado

print("\n❌ Retiro mayor al saldo:")
saldo = retirar_dinero(saldo, 200) # Error controlado
