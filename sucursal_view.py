from prettytable import PrettyTable
from sucursal_logic import SucursalLogic

logic = SucursalLogic()


def viewAllSucursales():
    sucursalObjList = logic.getAllSucursales()
    table = PrettyTable()
    table.field_names = [
        "Id",
        "Nombre",
        "Departamento",
        "Direccion",
        "usuario_idusuario",
    ]

    for sucursal in sucursalObjList:
        table.add_row(
            [
                sucursal.idsucursal,
                sucursal.nombre,
                sucursal.departamento,
                sucursal.direccion,
                sucursal.usuario_idusuario,
            ]
        )
    print(table)


def addSucursal():
    print("Ingrese nueva sucursal")
    nombre = input("nombre:")
    departamento = input("departamento:")
    direccion = input("direccion:")
    usuario_idusuario = input("idusuario: ")

    logic.createSucursalObj(nombre, departamento, direccion, usuario_idusuario)
    logic.insertSucursal(nombre, departamento, direccion, usuario_idusuario)
    logic.getAllSucursales()


def updateSucursal():
    print("Actualice la sucursal")
    id = int(input("Id de la sucursal a actualizar: "))
    sucursal = logic.updateSucursalById(id)

    update = int(input("¿Actualizar Nombre? Si -1 No - 0 "))
    if update == 1:
        print(f"Nombre anterior: {sucursal['nombre']}")
        nombre = input("nombre: ")
    else:
        nombre = sucursal["nombre"]

    update = int(input("Actualizar departamento? Si -1 No - 0 "))
    if update == 1:
        print(f"Departamento anterior: {sucursal['departamento']}")
        departamento = input("departamento: ")
    else:
        departamento = sucursal["departamento"]

    update = int(input("Actualizar direccion? Si -1 No - 0 "))
    if update == 1:
        print(f"Direccion anterior: {sucursal['direccion']}")
        direccion = input("direccion: ")
    else:
        direccion = sucursal["direccion"]

    update = int(input("Actualizar idusuario? Si -1 No - 0 "))
    if update == 1:
        print(f"Usuario anterior: {sucursal['usuario_idusuario']}")
        direccion = input("idusuario: ")
    else:
        direccion = sucursal["usuario_idusuario"]


def deleteSucursal():
    print("Eliminar sucursal")
    id = int(input("Id de la sucursal a eliminar: "))

    logic.deleteSucursalById(id)
