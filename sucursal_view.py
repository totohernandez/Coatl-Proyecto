from prettytable import PrettyTable
# from peliculas_logic import PeliculasLogic
from sucursal_logic import SucursalLogic
from sucursal_logic import(
    getAllSucursales,
    createSucursalObj,
    insertSucursal,
    updateSucursalById,
    deleteSucursalById,
)

def viewAllSucursales():
    sucursalObjList = getAllSucursales()
    table = PrettyTable()
    table.field_names = ["Id", "Nombre", "Departamento", "Direccion"]

    for sucursal in sucursalObjList:
        table.add_row([sucursal["id"], sucursal["Titulo"], sucursal["Descripcion"], sucursal["Fecha"], sucursal["Hora"]])
    print(table)


def addSucursal():
    print("Ingrese nueva sucursal")
    nombre = input("nombre:")
    departamento = input("departamento:")
    direccion = input("direccion:")
    
    createSucursalObj(nombre, departamento, direccion)
    insertSucursal(nombre, departamento, direccion)
    getAllSucursales()

def updateSucursal():
    print("Actualice la sucursal")
    id = int(input ("Id de la sucursal a actualizar: "))
    sucursal = updateSucursalById(id)

    update = int(input("Actualizar Nombre? Si -1 No - 0 "))
    if update == 1:
        print(f"Nombre viejo: {sucursal['nombre']}")
        nombre = input("nombre: ")
    else:
        nombre = sucursal["nombre"]

    update = int(input("Actualizar departamento? Si -1 No - 0 "))
    if update == 1:
        print(f"Departamento viejo: {sucursal['departamento']}")
        departamento = input("departamento: ")
    else:
        departamento = sucursal["departamento"]

    update = int(input("Actualizar direccion? Si -1 No - 0 "))
    if update == 1:
        print(f"Direccion vieja: {sucursal['direccion']}")
        direccion = input("direccion: ")
    else:
        direccion = sucursal["direccion"]

def deleteSucursal():
    print("Eliminar sucursal")
    id = int(input("ID de la sucursal a eliminar: "))

    deleteSucursalById(id)