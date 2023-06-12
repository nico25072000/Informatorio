#A partir del siguiente diagrama de clases, implementá clases y métodos para mostrar atributos.

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def imprimir_color(self):
        print(f"Color: {self.color}")
        
    def imprimir_ruedas(self):
        print(f"Ruedas: {self.ruedas}")
        
    def mostrar_atributos(self):
        print("Atributos coche:")
        self.imprimir_color()
        self.imprimir_ruedas()
        
# vehiculo1 = Vehiculo("Rojo", 2)

# print("vehiculo1: ")
# print("color:", vehiculo1.color)
# print("ruedas:", vehiculo1.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
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
        
        
coche1 = Coche("Negro", 4, 150, 2000)
coche1.mostrar_atributos()