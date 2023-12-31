import pickle

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def serializar_objeto(objeto, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(objeto, archivo)
    print(f"Objeto serializado y almacenado en {nombre_archivo}")

def deserializar_objeto(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        objeto = pickle.load(archivo)
    return objeto

# Ejemplo de uso
# Crear un objeto de la clase Persona
persona_original = Persona(nombre="Juan", edad=30)

# Serializar y almacenar el objeto en un archivo binario de extensión pickle
serializar_objeto(persona_original, 'persona.pkl')

# Deserializar el objeto desde el archivo
persona_recuperada = deserializar_objeto('persona.pkl')

# Imprimir la información del objeto original y del objeto recuperado
print("Objeto original:")
print(f"Nombre: {persona_original.nombre}, Edad: {persona_original.edad}")

print("\nObjeto recuperado:")
print(f"Nombre: {persona_recuperada.nombre}, Edad: {persona_recuperada.edad}")
