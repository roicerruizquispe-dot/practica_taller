"""ModuloArchivo: persistencia en archivo de texto plano (atenciones.txt)."""

ARCHIVO = "atenciones.txt"


def GuardarAtencion(linea):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(linea + "\n")


def BuscarAtencion(placaBuscada):
    encontrados = 0
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                campos = linea.split("|")
                if len(campos) == 5 and campos[0].upper() == placaBuscada.strip().upper():
                    encontrados += 1
                    print(f"\nPlaca:       {campos[0]}")
                    print(f"Propietario: {campos[1]}")
                    print(f"Servicio:    {campos[2]}")
                    print(f"Total:       S/ {campos[3]}")
                    print(f"Fecha:       {campos[4]}")
    except FileNotFoundError:
        print("Aún no existe el archivo atenciones.txt (no hay registros).")
        return
    if encontrados == 0:
        print("No se encontraron atenciones para esa placa.")
    else:
        print(f"\nCoincidencias encontradas: {encontrados}")


def ListarTodasLasAtenciones():
    total_recaudado = 0.0
    cantidad = 0
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            print(f"\n{'PLACA':<10}{'PROPIETARIO':<22}{'SERVICIO':<14}{'TOTAL (S/)':>12}  FECHA")
            print("-" * 75)
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                campos = linea.split("|")
                if len(campos) != 5:
                    continue
                cantidad += 1
                total_recaudado += float(campos[3])
                print(f"{campos[0]:<10}{campos[1]:<22}{campos[2]:<14}{float(campos[3]):>12.2f}  {campos[4]}")
    except FileNotFoundError:
        print("Aún no existe el archivo atenciones.txt (no hay registros).")
        return
    print("-" * 75)
    print(f"Vehículos atendidos: {cantidad}")
    print(f"Total recaudado por el taller: S/ {total_recaudado:.2f}")
