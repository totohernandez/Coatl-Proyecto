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
        "Dirección",
        "Usuario_idusuario",
    ]

    for sucursal in sucursalObjList:
        table.add_row(
            [
                sucursal["idsucursal"],
                sucursal["nombre"],
                sucursal["departamento"],
                sucursal["direccion"],
                sucursal["usuario_idusuario"],
            ]
        )
    print(table)


def addSucursal():
    print("Ingrese nueva sucursal")
    nombre = input("Nombre sucursal:")
    departamento = input("Departamento:")
    direccion = input("Direccion:")
    usuario_idusuario = input("IdUsuario: ")

    logic.createSucursalObj(nombre, departamento, direccion, usuario_idusuario)
    logic.insertSucursal(nombre, departamento, direccion, usuario_idusuario)
    print("Sucursal creada con éxito")


def updateSucursal():
    print("Actualice la sucursal")
    idsucursal = int(input("Id de sucursal a actualizar: "))
    oldSucursal = logic.getSucursalById(idsucursal)

    update = int(input("¿Desea actualizar el nombre? Si - 1 No - 0 "))
    if update == 1:
        print(f"Nombre anterior: {oldSucursal['nombre']}")
        nombre = input("Ingrese el nuevo nombre de la película: ")
    else:
        nombre = oldSucursal["nombre"]

    update = int(input("¿Desea actualizar el departamento? Si - 1 No - 0 "))
    if update == 1:
        print(f"Departamento anterior: {oldSucursal['departamento']}")
        departamento = input("departamento: ")
    else:
        departamento = oldSucursal.departamento

    update = int(input("¿Desea actualizar la dirección? Si - 1 No - 0 "))
    if update == 1:
        print(f"Direccion anterior: {oldSucursal['direccion']}")
        direccion = input("direccion: ")
    else:
        direccion = oldSucursal["direccion"]

    update = int(input("¿Desea actualizar el id de usuario? Si - 1 No - 0 "))
    if update == 1:
        print(f"Usuario anterior: {oldSucursal['usuario_idusuario']}")
        usuario_idusuario = int(input("idusuario: "))
    else:
        usuario_idusuario = oldSucursal["usuario_idusuario"]

    sucursal = logic.updateSucursalById(
        idsucursal, nombre, departamento, direccion, usuario_idusuario
    )
    print("La información de la sucursal ha sido actualizada")


def deleteSucursal():
    print("Eliminar sucursal")
    idsucursal = int(input("Id de sucursal a eliminar: "))
    logic.deleteSucursalById(idsucursal)
    print("Sucursal eliminada con éxito")
