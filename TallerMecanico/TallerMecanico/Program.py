from datetime import datetime
from FacturacionTaller import ModuloTaller, ModuloArchivo


def pedir_texto(mensaje):
    valor = input(mensaje).strip()
    if not valor:
        raise ValueError("El campo no puede estar vacío.")
    if "|" in valor:
        raise ValueError("El carácter '|' no está permitido.")
    return valor


def registrar_atencion():
    placa = pedir_texto("Placa: ").upper()
    propietario = pedir_texto("Propietario: ")
    tipo = pedir_texto("Tipo de servicio (PREVENTIVO / CORRECTIVO / OTRO): ").upper()
    frecuente = pedir_texto("¿Cliente frecuente? (SI/NO): ").upper()
    if frecuente not in ("SI", "NO"):
        raise ValueError("Debe ingresar SI o NO.")

    tarifa = ModuloTaller.ObtenerTarifaBase(tipo)
    descuento = ModuloTaller.CalcularDescuentoCliente(tarifa, frecuente)
    igv = ModuloTaller.CalcularImpuestoIGV(tarifa - descuento)
    total = ModuloTaller.CalcularTotalPagar(tarifa, descuento, igv)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linea = ModuloTaller.ConstruirRegistroPipe(placa, propietario, tipo, total, fecha)
    ModuloArchivo.GuardarAtencion(linea)

    print(f"\nTarifa base: S/ {tarifa:.2f}")
    print(f"Descuento:   S/ {descuento:.2f}")
    print(f"IGV (18%):   S/ {igv:.2f}")
    print(f"TOTAL:       S/ {total:.2f}")
    print("Atención registrada correctamente.")


def main():
    while True:
        print("\n===== TALLER MECÁNICO =====")
        print("1. Registrar atención")
        print("2. Buscar atención por Placa")
        print("3. Reporte general de atenciones")
        print("4. Salir")
        try:
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                registrar_atencion()
            elif opcion == "2":
                ModuloArchivo.BuscarAtencion(pedir_texto("Placa a buscar: "))
            elif opcion == "3":
                ModuloArchivo.ListarTodasLasAtenciones()
            elif opcion == "4":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida. Elija entre 1 y 4.")
        except ValueError as e:
            print(f"Error de entrada: {e}")
        except OSError as e:
            print(f"Error de archivo: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
