#realizarás operaciones de lectura y escritura en archivos de texto en Python

# Creamos un nuevo archivo llamado my_notes.txt y escribimos notas personales en él.

# Abrimos el archivo en modo escritura ('w')
with open ("my_notes.txt", "w") as file:
    with open("my_notes.txt", "w") as file:
        file.write("------lista de cosas por hacer o recordar------.\n")
        file.write("nota 1: recoger a maria del cole.\n")
        file.write("nota 2: estatura de maria 1.50m .\n")
        file.write("nota 3: comprar comida para la semana.\n")
        file.write("nota 4: presentar la tarea de programecion.\n")
        file.write("nota 5: llamar a mama y papa.\n")
        file.write("nota 6: adelantar la tarea de matematicas.\n")

    # Lectura del archivo my_notes.txt
    with open("my_notes.txt", "r") as file:
        # Leer línea por línea
        for line in file:
            print(line.strip())  # strip() elimina los saltos de línea adicionales
#No es necesario cerrar el archivo manualmente cuando se usa 'with',
# ya que se cierra automáticamente al salir del bloque