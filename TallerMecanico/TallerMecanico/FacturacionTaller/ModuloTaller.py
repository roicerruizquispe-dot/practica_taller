"""ModuloTaller: lógica de cálculo de tarifas, descuento, IGV y registro."""

IGV_TASA = 0.18
DESCUENTO_FRECUENTE = 0.15


def ObtenerTarifaBase(tipoServicio):
    tipo = tipoServicio.strip().upper()
    if tipo == "PREVENTIVO":
        return 180.00
    elif tipo == "CORRECTIVO":
        return 320.00
    else:
        return 120.00


def CalcularDescuentoCliente(tarifaBase, esFrecuente):
    if esFrecuente.strip().upper() == "SI":
        return tarifaBase * DESCUENTO_FRECUENTE
    return 0.0


def CalcularImpuestoIGV(tarifaBaseConDescuento):
    return tarifaBaseConDescuento * IGV_TASA


def CalcularTotalPagar(tarifaBase, descuento, igv):
    return tarifaBase - descuento + igv


def ConstruirRegistroPipe(placa, propietario, tipoServicio, totalPagar, fecha):
    return f"{placa}|{propietario}|{tipoServicio}|{totalPagar:.2f}|{fecha}"
