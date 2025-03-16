#Practicar la definición y uso de funciones en Python para calcular temperaturas promedio
#

def temperatura_promedio(ciudades_temperaturas): #funcion para calcular la temperatura
    temperaturas_promedio = {}

    for ciudad, semanas in ciudades_temperaturas.items():
        todas_las_temperaturas = []

        for semana in semanas:
            for dia in semana:
                todas_las_temperaturas.append(dia["temperatura"])  # Extraemos la temperatura

        promedio = sum(todas_las_temperaturas) / len(todas_las_temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "paltas": [
        [  # semana 1
            {"day": "lunes", "temperatura": 15},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 19},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 21},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 19},
            {"day": "viernes", "temperatura": 19},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 21},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 15},
            {"day": "miercoles", "temperatura": 20},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 23},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 22},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 20},
            {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 20},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 21},
            {"day": "sabado", "temperatura": 27},
            {"day": "domingo", "temperatura": 26},
        ]
    ],
    "loja": [
        [  # semana 1
            {"day": "lunes", "temperatura": 13},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 19},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 22},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 20},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 21},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 17},
            {"day": "miercoles", "temperatura": 18},
            {"day": "jueves", "temperatura": 20},
            {"day": "viernes", "temperatura": 22},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 24},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 20},
            {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 19},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 23},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 18},
        ]
    ],
    "catamayo": [
        [  # semana 1
            {"day": "lunes", "temperatura": 18},
            {"day": "martes", "temperatura": 28},
            {"day": "miercoles", "temperatura": 28},
            {"day": "jueves", "temperatura": 28},
            {"day": "viernes", "temperatura": 28},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 29},
            {"day": "martes", "temperatura": 30},
            {"day": "miercoles", "temperatura": 29},
            {"day": "jueves", "temperatura": 29},
            {"day": "viernes", "temperatura": 29},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 29},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 27},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 26},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 20},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 23},
            {"day": "sabado", "temperatura": 27},
            {"day": "domingo", "temperatura": 28},
        ]
    ]

}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio de las 4 semanas por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():

    print(f"{ciudad}: {promedio:.2f}°C")
