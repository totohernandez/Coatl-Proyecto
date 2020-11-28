from peliculas_view import viewAllPeliculas, addPelicula, updatePelicula, deletePelicula
from compradetallada_view import addCompra, viewAllCompras, updateCompra, deleteCompra
from boleto_view import addBoleto, viewAllBoletos, deleteBoleto
from sucursal_view import (
    viewAllSucursales,
    addSucursal,
    updateSucursal,
    deleteSucursal,
)
from asiento_view import (
    viewAllAsientos,
    addAsiento,
    updateAsiento,
    deleteAsiento,
)
from sala_view import (
    viewAllSalas,
    addSala,
    updateSala,
    deleteSala,
)


def goToSucursalesSubMenu():
    while True:
        print("Sucursal")
        print("Menu: ")
        print("0 - Salir: ")
        print("1 - Ver Sucursal: ")
        print("2 - Agregar Sucursal: ")
        print("3 - Actualizar Sucursal: ")
        print("4 - Borrar Sucursal: ")
        option = int(input("option: "))

        if option == 0:
            print("Salir de sucursales..")
            break
        if option == 1:
            viewAllSucursales()
        if option == 2:
            addSucursal()
        if option == 3:
            updateSucursal()
        if option == 4:
            deleteSucursal()


def goToAsientosSubMenu():
    while True:
        print("Asientos")
        print("Menu: ")
        print("0 - Salir: ")
        print("1 - Ver Asientos: ")
        print("2 - Agregar Asiento: ")
        print("3 - Actualizar Asiento: ")
        print("4 - Eliminar Asiento: ")
        option = int(input("option: "))

        if option == 0:
            print("Salir de selección de asientos")
            break
        if option == 1:
            viewAllAsientos()
        if option == 2:
            addAsiento()
        if option == 3:
            updateAsiento()
        if option == 4:
            deleteAsiento()


def goToSalaSubMenu():
    while True:
        print("Sala")
        print("Menu: ")
        print("0 - Salir: ")
        print("1 - Ver Sala: ")
        print("2 - Agregar Sala: ")
        print("3 - Actualizar Sala: ")
        print("4 - Borrar Sala: ")
        option = int(input("option: "))

        if option == 0:
            print("Salir de selección de sala:")
            break
        if option == 1:
            viewAllSalas()
        if option == 2:
            addSala()
        if option == 3:
            updateSala()
        if option == 4:
            deleteSala()


def goToPeliculasSubMenu():
    while True:
        print("Menú Películas")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver Peliculas: ")
        print("2 - Agregar Pelicula: ")
        print("3 - Actualizar Pelicula: ")
        print("4 - Borrar Pelicula: ")
        optionPelicula = int(input("Seleccione una opción: "))

        if optionPelicula == 0:
            print("Regresando a menú principal")
            break
        if optionPelicula == 1:
            viewAllPeliculas()
        if optionPelicula == 2:
            addPelicula()
        if optionPelicula == 3:
            updatePelicula()
        if optionPelicula == 4:
            deletePelicula()


def goToBoletoSubMenu():
    while True:
        print("Menú Boletos: ")
        print("0 - Regresar a menú principal: ")
        print("1 - Crear boleto (reserva): ")
        print("2 -Ver todos los boletos: ")
        optionBoleto = int(input("Seleccione una opción: "))

        if optionBoleto == 0:
            print("Regresando a menú principal")
            break
        elif optionBoleto == 1:
            addBoleto()
        elif optionBoleto == 2:
            viewAllBoletos()


while True:
    print("Bienvenid@ a la app cine")
    print("Menú: ")
    print("0 - Salir de la app: ")
    print("1 - Usuario: ")
    print("2 - Sucursales: ")
    print("3 - Peliculas: ")
    print("4 - Salas: ")
    print("5 - Asientos: ")
    print("6 - Boletos: ")
    print("7 - Detalle de compra: ")
    option = int(input("Seleccione una opción: "))

    if option == 0:
        print("Saliste de la aplicación")
        break
    if option == 1:
        pass
    if option == 2:
        goToSucursalesSubMenu()
    if option == 3:
        goToPeliculasSubMenu()
    if option == 4:
        goToSalaSubMenu()
    if option == 5:
        goToAsientosSubMenu()
    if option == 6:
        goToBoletoSubMenu()
    if option == 7:
        pass
