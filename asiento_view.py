from prettytable import PrettyTable
from asiento_logic import AsientoLogic

logic = AsientoLogic()


def viewAllAsientos():
    asientosObjList = logic.getAllAsientos()
    table = PrettyTable()
    table.field_names = ["idasiento", "silla_numero", "fila_letras"]

    for asiento in asientosObjList:
        table.add_row([asiento.idasiento, asiento.silla_numero, asiento.fila_letras])
    print(table)


def addAsiento():
    print("Ingrese el número de asiento y la letra de fila")
    silla_numero = input("Número de asiento:")
    fila_letras = input("Letra de fila:")

    logic.createAsientoObj(silla_numero, fila_letras)
    logic.insertAsiento(silla_numero, fila_letras)
    logic.getAllAsientos()


def updateAsiento():
    print("Actualización de asiento")
    id = int(input("Id de asiento a actualizar: "))
    asiento = logic.updateAsientoById(id)

    update = int(
        input(
            "¿Desea actualizar el número de asiento? Presione 1 para actualizar o 2 para conservar la localización del asiento: "
        )
    )
    if update == 1:
        print(f"Número anterior: {asiento['silla_numero']}")
        newNumber = input("Escriba el nuevo número de asiento: ")
    else:
        newNumber = asiento["silla_numero"]

    update = int(
        input(
            "¿Desea actualizar la letra de fila? Presione 1 para actualizar o 2 para conservar la localización de la fila: "
        )
    )
    if update == 1:
        print(f"Número anterior: {asiento['fila_letras']}")
        newLetter = input("Escriba el nuevo número de asiento: ")
    else:
        newLetter = asiento["fila_letras"]


def deleteAsiento():
    print("Eliminación de asiento")
    id = int(input("Id de asiento a eliminar: "))
    logic.deleteAsientoById(id)