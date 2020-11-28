from prettytable import PrettyTable
from peliculas_logic import PeliculasLogic


logic = PeliculasLogic()


def viewAllPeliculas():
    peliculasObjList = logic.getAllPeliculas()
    table = PrettyTable()
    table.field_names = ["idpeliculas", "titulo", "descripcion", "fecha", "hora"]

    for peliculas in peliculasObjList:
        table.add_row(
            [
                peliculas.idpeliculas,
                peliculas.titulo,
                peliculas.descripcion,
                peliculas.fecha,
                peliculas.hora,
            ]
        )
    print(table)


def addPelicula():
    print("Ingrese nueva pelicula")
    titulo = input("titulo:")
    descripcion = input("descripcion:")
    fecha = input("fecha:")
    hora = input("hora: ")

    logic.createPeliculasObj(titulo, descripcion, fecha, hora)
    logic.insertPeliculas(titulo, descripcion, fecha, hora)
    logic.getAllPeliculas()


def updatePelicula():
    print("Actualice pelicula")
    id = int(input("Id de pelicula a actualizar: "))
    pelicula = logic.updatePeliculasById(id)

    update = int(input("ACtualizar Titulo? Si -1 No - 0 "))
    if update == 1:
        print(f"Titulo anterior: {pelicula['titulo']}")
        name = input("titulo: ")
    else:
        name = pelicula["name"]

    update = int(input("Actualizar Descripcion? Si - 1 No - 2 "))
    if update == 1:
        print(f"Descripcion anterior: {pelicula['descripcion']}")
        descripcion = int(input("descricpion: "))
    else:
        descripcion = pelicula["descripcion"]

    update = int(input("Actualizar Fecha? Si - 1 No - 2 "))
    if update == 1:
        print(f"Fecha anterior: {pelicula['fecha']}")
        fecha = int(input("fecha: "))
    else:
        fecha = pelicula["fecha"]


def deletePelicula():
    print("Eliminar Pelicula")
    id = int(input("ID de la pelicula a eliminar: "))
    logic.deletePeliculasById(id)
    logic.getAllPeliculas()
