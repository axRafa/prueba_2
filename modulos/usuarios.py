import json

def registro(datos):

  usuario = input("Ingrese el nombre de usuario: ")
  contra = input("Ingrese la contraseña: ")

  datos[usuario] = contra


def leerData(datos):
  print("La info almacenada en la base de datos es:")
  for key, value in datos.items():
    print(key, value)

def login(datos):

  nombre = input("Ingrese su usuario: ")

  if nombre in datos.keys():
    clave = input("Ingrese su contraseña: ")

    if datos[nombre] == clave:
      return "Has iniciado sesión"

    else:
      return "Contraseña incorrecta"
      
  else:
    return "No se ha encontrado el usuario"


def guardarArchivo(datos):

  with open(ruta+"archivo.txt", "w") as file:
    json.dump(datos, file, indent=4)