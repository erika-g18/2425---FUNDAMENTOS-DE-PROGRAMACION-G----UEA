#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
#En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

temperaturas = [
    [ #paltas
        [#semana 1 del 10 al 16 de marzo 2025
            {"day": "lunes", "temperatura": 15},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 19},
        ],
        [#semana 2 del 17 al 23 de marzo del 2025
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 21},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 19},
            {"day": "viernes", "temperatura": 19},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 21},
         ]
    ],
    [#loja
            [ #semana 1 del 10 al 16 de marzo del 2025
            {"day":"lunes","temperatura":13},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 19},
              ],
            [# semana 2 del 17 al 23 de marzo 2025
                {"day":"lunes","temperatura":19},
                {"day": "martes", "temperatura": 22},
                {"day": "miercoles", "temperatura": 21},
                {"day": "jueves", "temperatura": 20},
                {"day": "viernes", "temperatura": 20},
                {"day": "sabado", "temperatura": 19},
                {"day": "domingo", "temperatura": 21},
            ]
    ],
    [#catamayo
            [ #semana 1 del 10 al 16 de marzo del 2025
            {"day":"lunes","temperatura":18},
            {"day": "martes", "temperatura": 28},
            {"day": "miercoles", "temperatura": 28},
            {"day": "jueves", "temperatura": 28},
            {"day": "viernes", "temperatura": 28},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
              ],
            [# semana 2 del 17 al 23 de marzo 2025
                {"day":"lunes","temperatura":29},
                {"day": "martes", "temperatura": 30},
                {"day": "miercoles", "temperatura": 29},
                {"day": "jueves", "temperatura": 29},
                {"day": "viernes", "temperatura": 29},
                {"day": "sabado", "temperatura": 29},
                {"day": "domingo", "temperatura": 29},
            ]
    ]
]
#nombres de la cuidad
nombres_ciudades = ["paltas", "loja", "catamayo"]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum(day["temperatura"] for day in semana)
        promedio = suma_temperaturas / len(semana)
        print(f"El promedio de temperatura de {nombres_ciudades[ciudad_idx]}, semana {semana_idx + 1}: promedio {promedio:.2f}")