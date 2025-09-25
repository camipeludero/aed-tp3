from funciones import *

def menu():
    print("--MENU--")
    print("1-Cargar envios.")
    print("2- Mostrar resultados.")
    print("0- Salir.")
    print()
    op = int(input("Ingrese opción: "))
    return op


def cargar_datos():
    archivo = open("envios.csv")
    linea = archivo.readline().strip()
    v = []


    while linea != "":

        linea_sp = linea.split(",")
        cod_og, cod_pago, id_pago, id_dest, nom_dest, tasa, monto_nom, id_algcom, id_algimp = linea_sp[0].split("|")[0], linea_sp[0].split("|")[1], linea_sp[0].split("|")[2], linea_sp[1], linea_sp[2], float(linea_sp[3]), int(linea_sp[4]), int(linea_sp[5]), int(linea_sp[6])

        v.append(Envio(cod_og, cod_pago, id_pago, id_dest, nom_dest, tasa, monto_nom, id_algcom, id_algimp))

        linea = archivo.readline().strip()



    archivo.close()
    return v


def envios_distinta_moneda(v):
    n = len(v)
    c = 0
    for i in range(n):
        if v[i].codigo_moneda_pago != v[i].codigo_moneda_origen:
            c += 1
    return c


def porcentaje_promedio(v):
    pp = 0
    n = len(v)
    ac = 0

    for r in v:
        comision = calcular_comision(r.monto_nominal, r.id_algoritmo_comision)
        porcentaje_comision = comision * 100 // r.monto_nominal
        ac += porcentaje_comision

    if n > 0:
        pp = ac // n
    return pp


def mayor_descuento(v):
    mayor_porcentaje = None
    id_mayor = None
    envio_mayor = None

    for r in v:
        porc_descuento = calcular_porcentaje_descuento(r)
        if mayor_porcentaje is None or porc_descuento > mayor_porcentaje:
            mayor_porcentaje = porc_descuento
            id_mayor = r.id_pago
            envio_mayor = r

    monto_final = calcular_monto_final_convertido(envio_mayor)

    return id_mayor, monto_final


def mostrar(v):
    pp = porcentaje_promedio(v)
    id_mayor, mayor = mayor_descuento(v)
    print(f"r2.1: {pp}")
    print(f"r2.2: {id_mayor}")
    print(f"r2.3: {mayor}")

def main():

    v = []
    op = -1

    while op != 0:
        op = menu()

        if op == 1:

            v = cargar_datos()
            print(f"r1.1: {len(v)}")
            print(f"r1.2: {envios_distinta_moneda(v)}")


        elif op == 2:

            if v:
                mostrar(v)
            else:
                print("No hay datos cargados.")

        elif op == 0:
            print("Programa finalizado.")

        else:
            print("Opción invalida.")


if __name__ == "__main__":
    main()