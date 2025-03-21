# Clase Base 1
class SerVivo:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def crecer(self):
        print(f"{self.nombre} está creciendo...")

# Clase Base 2
class Flora:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def fotosintesis(self):
        print(f"La {self.tipo} está realizando la fotosíntesis.")

# Clase derivada (hereda de SerVivo y Flora)
class Planta(SerVivo, Flora):
    def __init__(self, nombre, edad, tipo):
        # Inicializamos las clases base
        SerVivo.__init__(self, nombre, edad)
        Flora.__init__(self, tipo)

    def mostrar_info(self):
        print(f"Planta: {self.nombre}, Edad: {self.edad} años, Tipo: {self.tipo}")
        
# Crear una instancia de Planta
planta = Planta("Rosa", 2, "flor")
planta.mostrar_info()  # Mostrar información de la planta
planta.crecer()        # Método de SerVivo
planta.fotosintesis()  # Método de Flora

# Clase Base 1
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

# Clase Base 2
class Electrico:
    def __init__(self, autonomia):
        self.autonomia = autonomia
    
    def mostrar_autonomia(self):
        print(f"Autonomía: {self.autonomia} km")

# Clase derivada (hereda de Vehiculo y Electrico)
class CocheElectrico(Vehiculo, Electrico):
    def __init__(self, marca, modelo, autonomia):
        # Inicializamos las clases base
        Vehiculo.__init__(self, marca, modelo)
        Electrico.__init__(self, autonomia)

# Crear una instancia de CocheElectrico
coche = CocheElectrico("Tesla", "Model 3", 500)

# Usar los métodos de las clases base
coche.mostrar_informacion()  # Método de Vehiculo
coche.mostrar_autonomia()    # Método de Electrico