from boleto_logic import BoletoLogic
from compradetallada_view import deleteCompra
from prettytable import PrettyTable

logic = BoletoLogic()


def addBoleto():
    print("Ingrese una nueva reserva(boleto)")
    tipo = input("Tipo: ")
    fecha = input("Fecha: ")
    hora = input("Hora: ")
    compradetallada_idcompra = input("Id de compra ")
    sala_idsala = input("Id de sala ")
    peliculas_idpeliculas = input("Id de pelicula: ")

    logic.createBoletoObj(
        tipo, fecha, hora, compradetallada_idcompra, sala_idsala, peliculas_idpeliculas
    )
    logic.insertBoleto(
        tipo, fecha, hora, compradetallada_idcompra, sala_idsala, peliculas_idpeliculas
    )
    logic.getAllBoletos()


def viewAllBoletos():
    boletosObjList = logic.getAllBoletos()
    table = PrettyTable()
    table.field_names = [
        "idboleto",
        "tipo",
        "fecha",
        "hora",
        "compradetallada_idcompra",
        "sala_idsala",
        "peliculas_idpeliculas",
    ]

    for compras in boletosObjList:
        table.add_row(
            [
                compras.idboleto,
                compras.tipo,
                compras.fecha,
                compras.hora,
                compras.compradetallada_idcompra,
                compras.sala_idsala,
                compras.peliculas_idpeliculas,
            ]
        )
    print(table)


def deleteBoleto():
    while deleteCompra:
        logic.deleteBoletoById(id)