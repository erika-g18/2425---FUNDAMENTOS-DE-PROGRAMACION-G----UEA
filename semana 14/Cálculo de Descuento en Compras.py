#El objetivo de esta tarea es practicar el uso de funciones en Python, incluyendo parámetros, valores predeterminados
#y retorno de valores. Deberás crear un programa que calcule el descuento en compras en
#función del monto total de la compra y mostrar el monto final a pagar

def calcular_descuento(monto_total, porcentaje_descuento=10):

    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final_sin_iva = monto_total - descuento
    return monto_final_sin_iva


def calcular_iva(monto_final_sin_iva, porcentaje_iva=15):
    """
    Calcula el IVA sobre el monto final sin IVA.

    :param monto_final_sin_iva: Monto final a pagar antes de IVA.
    :param porcentaje_iva: Porcentaje de IVA a aplicar (por defecto es 15%).
    :return: Monto del IVA.
    """
    iva = (monto_final_sin_iva * porcentaje_iva) / 100
    return iva


def main():
    # Solicitar al usuario el monto total de la compra
    monto_total = float(input("Ingrese el monto total de la compra: $"))

    # Solicitar al usuario el porcentaje de descuento (opcional)
    porcentaje_descuento = input("Ingrese el porcentaje de descuento (presione Enter para usar 10%): ")

    # Verificar si se ingresó un porcentaje de descuento
    if porcentaje_descuento:
        porcentaje_descuento = float(porcentaje_descuento)
    else:
        porcentaje_descuento = 10  # Valor predeterminado

    # Calcular el monto final a pagar antes de IVA
    monto_final_sin_iva = calcular_descuento(monto_total, porcentaje_descuento)

    # Calcular el IVA
    iva = calcular_iva(monto_final_sin_iva)

    # Calcular el monto total a pagar incluyendo IVA
    monto_final_con_iva = monto_final_sin_iva + iva

    # Mostrar el resultado
    print(
        f"El monto final a pagar después de aplicar un descuento del {porcentaje_descuento}% es: ${monto_final_sin_iva:.2f}")
    print(f"El IVA (15%) sobre el monto final es: ${iva:.2f}")
    print(f"El monto total a pagar incluyendo IVA es: ${monto_final_con_iva:.2f}")


# Ejecutar el programa
if __name__ == "__main__":
    main()



