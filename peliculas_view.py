from prettytable import PrettyTable
# from peliculas_logic import PeliculasLogic
from peliculas_logic import PeliculasLogic
from peliculas_logic import(
    getAllPeliculas,
    createPeliculasObj,
    insertPeliculas,
    updatePeliculasById,
    deletePeliculasById,
)

def viewAllPeliculas():
    peliculasObjList = getAllPeliculas()
    table = PrettyTable()
    table.field_names = ["Id", "Titulo", "Descripcion", "Fecha", "Hora"]

    for peliculas in peliculasObjList:
        table.add_row([peliculas["id"], peliculas["Titulo"], peliculas["Descripcion"], peliculas["Fecha"], peliculas["Hora"]])
    print(table)


def addPelicula():
    print("Ingrese nueva pelicula")
    titulo = input("titulo:")
    descripcion = input("descripcion:")
    fecha = input("fecha:")
    hora = input("hora: ")

    createPeliculasObj(titulo, descripcion, fecha, hora)
    insertPeliculas(titulo, descripcion, fecha, hora)
    getAllPeliculas()

def updatePelicula():
    print("Actualice pelicula")
    id = int(input ("Id de pelicula a actualizar: "))
    pelicula = updatePeliculasById(id)

    update = int(input("ACtualizar Titulo? Si -1 No - 0 "))
    if update == 1:
        print(f"Titulo viejo: {pelicula['titulo']}")
        name = input("titulo: ")
    else:
        name = pelicula["name"]

    update = int(input("Actualizar Descripcion? Si - 1 No - 2 "))
    if update == 1:
        print(f"Descripcion vieja: {pelicula['descripcion']}")
        descripcion = int(input("descricpion: "))
    else:
        descripcion = pelicula["descripcion"]

    update = int(input("Actualizar Fecha? Si - 1 No - 2 "))
    if update == 1:
        print(f"Fecha vieja: {pelicula['fecha']}")
        fecha = int(input("fecha: "))
    else:
        fecha = pelicula["fecha"]

def deletePeliculas():
    print("Eliminar Pelicula")
    id = int(input("ID de la pelicula a eliminar: "))

    deletePeliculasById(id)