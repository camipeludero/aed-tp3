class Envio:
    def __init__(self, cod_og, cod_pago, id_pago, id_dest, nom_dest, tasa, monto_nom, id_algcom, id_algimp):
        self.codigo_moneda_origen = cod_og
        self.codigo_moneda_pago = cod_pago
        self.id_pago = id_pago
        self.id_destinatario = id_dest
        self.nombre_destinatario = nom_dest
        self.tasa_conversion = tasa
        self.monto_nominal = monto_nom
        self.id_algoritmo_comision = id_algcom
        self.id_algoritmo_impositivo = id_algimp

def es_mayuscula(c):
    return 'A' <= c <= 'Z'

def es_digito(c):
    return c in '0123456789'

def validar_moneda(nro_cod):
    nro_cod = nro_cod.strip()
    ars = 0
    usd = 0
    jpy = 0
    eur = 0
    gbp = 0
    moneda = None

    if "ARS" in nro_cod:
        ars = 1
        moneda = "ARS"

    if "USD" in nro_cod:
        usd = 1
        moneda = "USD"

    if "JPY" in nro_cod:
        jpy = 1
        moneda = "JPY"

    if "EUR" in nro_cod:
        eur = 1
        moneda = "EUR"

    if "GBP" in nro_cod:
        gbp = 1
        moneda = "GBP"

    suma = ars + usd + jpy + eur + gbp

    if suma > 1 or suma == 0:
        moneda = "Moneda no valida."

    return moneda

def validar_numero_orden(num_codigo):
    num_codigo = num_codigo.strip()
    if num_codigo == '':
        return False

    valido = False
    for c in num_codigo:
        if es_mayuscula(c) or es_digito(c):
            valido = True
        elif c != '-':
            return False

    return valido


def calcular_comision_1(monto_nominal):
    return (monto_nominal * 9) // 100


def calcular_comision_2(monto_nominal):
    if monto_nominal < 50000:
        return 0
    elif 50000 <= monto_nominal < 80000:
        return (monto_nominal * 5) // 100
    else:
        return (monto_nominal * 7.8) // 100


def calcular_comision_3(monto_nominal):
    MONTO_FIJO = 100
    comision = 0
    if monto_nominal > 25000:
        comision = (monto_nominal * 6) // 100
    return MONTO_FIJO + comision


def calcular_comision_4(monto_nominal):
    if monto_nominal <= 100000:
        return 500
    else:
        return 1000


def calcular_comision_5(monto_nominal):
    comision = 0
    if monto_nominal >= 500000:
        comision = (monto_nominal * 7) // 100
    if comision > 50000:
        comision = 50000
    return comision


def calcular_comision_7(monto_nominal):
    comision = 0
    if monto_nominal <= 75000:
        comision = 3000
    else:
        comision = ((monto_nominal - 75000) * 5) // 100
    if comision > 10000:
        comision = 10000
    return comision


def calcular_comision(monto_nominal, n_algoritmo):
    if n_algoritmo == 1:
        return calcular_comision_1(monto_nominal)
    elif n_algoritmo == 2:
        return calcular_comision_2(monto_nominal)
    elif n_algoritmo == 3:
        return calcular_comision_3(monto_nominal)
    elif n_algoritmo == 4:
        return calcular_comision_4(monto_nominal)
    elif n_algoritmo == 5:
        return calcular_comision_5(monto_nominal)
    elif n_algoritmo == 7:
        return calcular_comision_7(monto_nominal)
    else:
        return monto_nominal

def calcular_monto_final_1(monto_base):
    impuesto = 0
    if monto_base > 300000:
        excedente = monto_base - 300000
        impuesto = (excedente * 25) // 100
    return monto_base - impuesto

def calcular_monto_final_2(monto_base):
    if monto_base < 50000:
        impuesto = 50
    else:
        impuesto = 100
    return monto_base - impuesto

def calcular_monto_final_3(monto_base):
    impuesto = (monto_base * 3) // 100
    return monto_base - impuesto

def calcular_monto_final(monto_base, n_algoritmo):
    if n_algoritmo == 1:
        return calcular_monto_final_1(monto_base)
    elif n_algoritmo == 2:
        return calcular_monto_final_2(monto_base)
    elif n_algoritmo == 3:
        return calcular_monto_final_3(monto_base)
    else:
        return monto_base


def calcular_monto_final_convertido(r):
    comision = calcular_comision(r.monto_nominal, r.id_algoritmo_comision)
    monto_base = r.monto_nominal - comision
    monto_final = calcular_monto_final(monto_base, r.id_algoritmo_impositivo)
    monto_final_convertido = int(monto_final * r.tasa_conversion)

    return monto_final_convertido

def calcular_promedio_entero(suma,cant):
    if cant > 0:
        return suma // cant
    return 0


def calcular_porcentaje_entero(cant,total):
    if total > 0:
        return (cant * 100) // total
    return 0

def calcular_porcentaje_descuento(r):
    comision = calcular_comision(r.monto_nominal, r.id_algoritmo_comision)
    monto_base = r.monto_nominal - comision
    monto_final = calcular_monto_final(monto_base, r.id_algoritmo_impositivo)
    descuento = r.monto_nominal - monto_final

    return descuento * 100 / r.monto_nominal
