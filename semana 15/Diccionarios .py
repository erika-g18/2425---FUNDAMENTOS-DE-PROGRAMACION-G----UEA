#Objetivo: Utilizar diccionarios en Python para representar información
# estructurada y realizar operaciones comunes.

#creamos un diccionaio llamado --informacion_personal--
informacion_personal= {"nombre": "Ariana", "edad": 22, "cuidad":"paltas",
                       "color favorito":"negro","pasatiempo":"correr","hermanos":2}

#imprimimos el diccionario original
print("*****diccionario original*****")
print("informacion personal:",informacion_personal)

#acceder al diccionario, con la palabra clave "cuidad" cambiamos el nombre de la cuidad por una diferente
informacion_personal["cuidad"]="Cuenca"
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["profesion"]="enfermera"

#Verifica si la clave "telefono" existe en el diccionario.
#Si no existe, agrégala con un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"]="0900000011"

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria
del informacion_personal["edad"]
#Imprime el diccionario resultante después de realizar todas las operaciones
print("\n*****diccionario modificado*****")
print("informacion personal:",informacion_personal)



