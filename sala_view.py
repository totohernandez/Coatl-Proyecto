from prettytable import PrettyTable
from sala_logic import SalaLogic

logic = SalaLogic()


def viewAllSalas():
    salasObjList = logic.getAllSalas()
    table = PrettyTable()
    table.field_names = ["idasala", "capacidad", "tipo"]

    for sala in salasObjList:
        table.add_row([sala.idsala, sala.capacidad, sala.tipo])
    print(table)


def addSala():
    capacidad = input("capacidad: ")
    tipo = input("tipo:")

    logic.createSalaObj(capacidad, tipo)
    logic.insertSala(capacidad, tipo)
    logic.getAllSalas()


def updateSala():
    print("Actualización de sala")
    id = int(input("Id de sala a actualizar: "))
    sala = logic.updateSalaById(id)

    update = int(
        input(
            "¿Desea actualizar el número sala? Presione 1 para actualizar o 2 para conservar la sala: "
        )
    )
    if update == 1:
        print(f"Sala anterior: {sala['tipo']}")
        newNumber = input("Escriba el Id de la nueva sala: ")
    else:
        newNumber = sala["tipo"]


def deleteSala():
    print("Eliminar sala")
    id = int(input("Id de sala a eliminar: "))
    logic.deleteSalaById(id)
