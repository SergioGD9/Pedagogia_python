"""
Script: herencia_vehiculos.py
Autor: Sergio
Descripción:
    Este script muestra un ejemplo pedagógico del uso de **herencia de clases** en Python.
    
    - Se define una clase base: VehiculoMotor
      con atributos y métodos comunes a cualquier vehículo con motor.
    
    - Se crean clases hijas que heredan de VehiculoMotor:
        - Coche
        - Moto
    
    - Cada subclase puede:
        1. Usar métodos heredados (ej: arrancar, parar).
        2. Añadir nuevos métodos específicos.
        3. Sobrescribir métodos de la clase base.
    
    Conceptos que se enseñan:
        ✔ Herencia simple
        ✔ Reutilización de código
        ✔ Polimorfismo (sobrescribir métodos)
        ✔ Métodos específicos de cada subclase
"""


class VehiculoMotor:
    """Clase base para representar un vehículo con motor."""

    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.en_taller = False
        self.combustible = 0

    def arrancar(self):
        """Arranca el motor si hay combustible disponible."""
        if self.combustible > 0 and not self.encendido:
            self.encendido = True
            print(f"{self.marca} {self.modelo} ha arrancado 🚀")
        elif self.encendido:
            print(f"{self.marca} {self.modelo} ya está en marcha.")
        else:
            print(f"{self.marca} {self.modelo} no puede arrancar, falta combustible ⛽")

    def parar(self):
        """Apaga el motor si está encendido."""
        if self.encendido:
            self.encendido = False
            print(f"{self.marca} {self.modelo} se ha parado 🛑")
        else:
            print(f"{self.marca} {self.modelo} ya estaba apagado.")

    def repostar(self, litros: int):
        """Añade combustible al depósito."""
        self.combustible += litros
        print(f"{self.marca} {self.modelo} ha repostado {litros} litros. Total: {self.combustible} litros ⛽")

    def ir_taller(self):
        """Lleva el vehículo al taller."""
        self.en_taller = True
        print(f"{self.marca} {self.modelo} está en el taller 🔧")

    def salir_taller(self):
        """Saca el vehículo del taller."""
        if self.en_taller:
            self.en_taller = False
            print(f"{self.marca} {self.modelo} ha salido del taller ✅")
        else:
            print(f"{self.marca} {self.modelo} no estaba en el taller.")


class Coche(VehiculoMotor):
    """Subclase que representa un coche, hereda de VehiculoMotor."""

    def tocar_claxon(self):
        """Método específico de los coches."""
        print(f"{self.marca} {self.modelo} dice: ¡Piiii piiii! 🚗📢")


class Moto(VehiculoMotor):
    """Subclase que representa una moto, hereda de VehiculoMotor."""

    def hacer_caballito(self):
        """Método específico de las motos."""
        if self.encendido:
            print(f"{self.marca} {self.modelo} está haciendo un caballito 🏍️🔥")
        else:
            print(f"No puedes hacer un caballito con la moto apagada 😅")


if __name__ == "__main__":
    # Crear objetos de cada clase
    coche1 = Coche("Toyota", "Corolla")
    moto1 = Moto("Yamaha", "MT-07")

    # Usar métodos de la clase base
    coche1.repostar(20)
    coche1.arrancar()
    coche1.parar()

    # Usar métodos específicos de Coche
    coche1.tocar_claxon()

    print("\n---\n")

    # Usar métodos en la Moto
    moto1.repostar(5)
    moto1.arrancar()
    moto1.hacer_caballito()
    moto1.ir_taller()
    moto1.salir_taller()
