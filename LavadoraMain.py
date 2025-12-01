from lavadoraEstandar import LavadoraEstandar
from lavadoraInteligente import LavadoraInteligente
from datetime import datetime

def main():

    print("\n     SISTEMA LAVA SMART     \n")

    # =============================
    # SELECCIÓN DE TIPO DE LAVADORA (PRIMERO, COMO PEDISTE)
    # =============================
    while True:
        try:
            print("\n1. Lavadora Estándar")
            print("2. Lavadora Inteligente")
            tipo = int(input("Seleccione el tipo de lavadora: "))

            if tipo == 1:
                tipo_lavadora_txt = "Estándar"
                break
            elif tipo == 2:
                tipo_lavadora_txt = "Inteligente"
                break
            else:
                print("Opción inválida.")
        except:
            print("Entrada inválida, ingrese 1 o 2.")

    print('-------------------------------------------------------------------')

    # =============================
    # DATOS DEL CLIENTE
    # =============================
    nombre = input("Ingrese su nombre: ")
    print('-------------------------------------------------------------------')

    # Validación de kilos
    while True:
        try:
            kilos = float(input("Ingrese los kilos de ropa: "))
            if kilos <= 4 or kilos > 40:
                print("Debe ingresar un número mayor a 4 y menor de 40.")
                continue
            break
        except:
            print("Entrada inválida, ingrese un número.")
    print('-------------------------------------------------------------------')

    # Tipo de ropa
    while True:
        try:
            tipo_ropa = int(input("Tipo de ropa (1 delicada - 2 normal - 3 pesada): "))
            if tipo_ropa not in [1, 2, 3]:
                print("Opción inválida, solo 1, 2 o 3.")
                continue
            break
        except:
            print("Debe ingresar un número entero.")
    print('-------------------------------------------------------------------')

    # Estrato
    while True:
        try:
            estrato = int(input("Estrato (1 a 6): "))
            if estrato < 1 or estrato > 6:
                print("Estrato inválido.")
                continue
            break
        except:
            print("Debe ingresar un número entero.")
    print('-------------------------------------------------------------------')

    # Tiempo de lavado
    while True:
        try:
            tiempo_lavado = int(input("Tiempo de lavado (min): "))
            if tiempo_lavado <= 0:
                print("Debe ser un número positivo.")
                continue
            break
        except:
            print("Entrada inválida.")
    print('-------------------------------------------------------------------')

    # Potencia
    while True:
        try:
            potencia = float(input("Potencia kW: "))
            if potencia <= 0:
                print("Ingrese un número mayor a 0.")
                continue
            break
        except:
            print("Entrada inválida.")
    print('-------------------------------------------------------------------')


    # =============================
    # CREACIÓN DE LA LAVADORA SEGÚN TIPO
    # =============================
    if tipo == 1:
        lavadora = LavadoraEstandar(kilos, estrato, tiempo_lavado, potencia, tipo_ropa)

    elif tipo == 2:
        # Orden corregido para la clase inteligente
        lavadora = LavadoraInteligente(kilos, estrato, tiempo_lavado, potencia, tipo_ropa)


    # =============================
    # CICLO DE LAVADO
    # =============================
    print("\n     Iniciando Ciclo     \n")
    print('-------------------------------------------------------------------')

    lavadora.encender()
    print('-------------------------------------------------------------------')

    if tipo == 2:
        print('Lavadora con conexión WiFi y sensores.')
    else:
        print('Lavadora estándar sin sensores ni WiFi.')
    print('-------------------------------------------------------------------')

    # Validar kilos
    print(lavadora._validar_kilos())
    print('-------------------------------------------------------------------')

    print(lavadora.mostrar_informacion())
    print('-------------------------------------------------------------------')

    print(lavadora._llenar())
    print('-------------------------------------------------------------------')

    print(lavadora._lavar())
    print('-------------------------------------------------------------------')

    print(lavadora._enjuagar())
    print('-------------------------------------------------------------------')

    secar = input("¿Desea secar? (s/n): ").lower()
    print('-------------------------------------------------------------------')

    if secar == "s":
        print(lavadora._secar())
    else:
        print("Secado omitido por el cliente.")
    print('-------------------------------------------------------------------')

    print(lavadora.ciclo_terminado())
    print('-------------------------------------------------------------------')

    # Cálculo total
    costo_total = lavadora.calcular_costo()

    # =============================
    # REPORTE CLIENTE
    # =============================
    print("\n===== REPORTE DEL CLIENTE =====")
    print(f"Cliente: {nombre}")
    print('-------------------------------------------------------------------')
    print(f"Fecha y hora: {datetime.now()}")
    print('-------------------------------------------------------------------')
    print(f"Kilos: {kilos}")
    print(f"Tipo de ropa: {tipo_ropa}")
    print(f"Método de lavado: {tipo_lavadora_txt}")
    print(f"Consumo total: {costo_total:.2f}")
    print("Gracias por usar Lava Smart.")
    print('-------------------------------------------------------------------')

    # =============================
    # REPORTE ADMINISTRADOR
    # =============================
    print("\n     ADMIN     ")
    print('-------------------------------------------------------------------')
    print(f"IVA cobrado: {lavadora.iva:.2f}")
    print(f"Ganancia neta: {lavadora.unidad_empresario():.2f}")
    print(f"Total facturado (energía): {lavadora.costo_energia():.2f}")
    print('-------------------------------------------------------------------')


if __name__ == "__main__":
    main()
