from Ejercicio_1 import *

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        
    def imprimir_carga(self):
        print(f"Carga: {self.carga}")
    
    def mostrar_atributos(self):
        super().mostrar_atributos()
        self.imprimir_carga()
        

# camioneta1 = Camioneta("Azul", 4, 160, 2300, 1000)
# camioneta1.mostrar_atributos()
# print("*"*40)
# coche1 = Coche("Azul", 4, 160, 2300)
# coche1.mostrar_atributos()

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def imprimir_tipo(self):
        print(f"Tipo: {self.tipo}")
    
    def mostrar_atributos(self):
        super().mostrar_atributos()
        self.imprimir_tipo()
        
# bici = Bicicleta("Verde", 2, "Urbana")
# bici.mostrar_atributos()

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def imprimir_velocidad(self):
        print(f"Velocidad: {self.velocidad}km/h")
        
    def imprimir_cilindrada(self):
        print(f"Cilindrada: {self.cilindrada}cc")
        
    def mostrar_atributos(self):
        super().mostrar_atributos()
        self.imprimir_velocidad()
        self.imprimir_cilindrada()
        
motocicleta = Motocicleta("Gris", 2, "Urbana", 80, 110)
motocicleta.mostrar_atributos()