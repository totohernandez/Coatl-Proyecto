from compradetallada_logic import CompraDetLogic
from prettytable import PrettyTable

logic = CompraDetLogic()


def addCompra():
    print("Ingrese una nueva compra")
    tipo = input("Tipo:")
    precios_unitarios = input("Precios unitarios:")
    cantidad = input("Cantidad:")
    monto_total = input("Monto total: ")
    estado = input("Estado de compra: ")

    logic.createCompraDetObj(tipo, precios_unitarios, cantidad, monto_total, estado)
    logic.insertCompra(tipo, precios_unitarios, cantidad, monto_total, estado)
    logic.getAllCompras()


def viewAllCompras():
    comprasObjList = logic.getAllCompras()
    table = PrettyTable()
    table.field_names = [
        "idcompra",
        "tipo",
        "precios_unitarios",
        "cantidad",
        "monto_total",
        "estado",
    ]

    for compras in comprasObjList:
        table.add_row(
            [
                compras["idcompra"],
                compras["tipo"],
                compras["precios_unitarios"],
                compras["cantidad"],
                compras["monto_total"],
                compras["estado"],
            ]
        )
    print(table)


def viewComprasById():
    comprasObjList = logic.getCompraById()
    table = PrettyTable()
    table.field_names = [
        "idcompra",
        "tipo",
        "precios_unitarios",
        "cantidad",
        "monto_total",
        "estado",
    ]

    for compras in comprasObjList:
        table.add_row(
            [
                compras.idcompra,
                compras.tipo,
                compras.precios_unitarios,
                compras.cantidad,
                compras.monto_total,
                compras.estado,
            ]
        )
    print(table)


def updateCompra():
    print("Actualice la compra")
    idcompra = int(input("Id de compra a actualizar: "))
    compra = logic.updateCompraById(idcompra)

    update = int(input("¿Actualizar estado? Si-1  No -0 "))
    if update == 1:
        print(f"Estado anterior: {compra['estado']}")
        name = input("Nuevo estado: ")
    else:
        name = compra["estado"]


def deleteCompra():
    print("Eliminar compra")
    id = int(input("Id de la pelicula a eliminar: "))
    logic.deleteCompraById(id)