from dx_logic import Logic
from peliculas_obj import PeliculasObj


class PeliculasLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "peliculas"

    def getAllPeliculas(self):
        peliculasList = super().getAllRows(self.tableName)
        peliculasObjList = []
        for element in peliculasList:
            newPeliculas = self.createPeliculasObj(element)
            peliculasObjList.append(newPeliculas)
        return peliculasObjList
    
    def createPeliculasObj(self, id, titulo, descripcion, fecha, hora):
        peliculasObj = PeliculasObj(id, titulo, descripcion, fecha, hora)
        return peliculasObj

    def createPeliculasObj(self, userDict):
        peliculasObj = PeliculasObj(
            userDict["titulo"],
            userDict["descripcion"],
            userDict["fecha"],
            userDict["hora"],
            userDict["id"],
        )
        return peliculasObj

    def insertPeliculas(self, titulo, descripcion, fecha, hora):
        database = self.database
        sql = (
            f"INSERT INTO `cine`.`peliculas`(`id`,`titulo`,`descripcion`,`fecha`, `hora`) "
            + f"VALUES(0,'{titulo}','{descripcion}','{fecha}','{hora}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updatePeliculasById(self, titulo, descripcion, fecha, hora):
        database = self.database
        sql = (
            "UPDATE `cine`.`peliculas` "
            + f"SET `titulo` = '{titulo}', `descripcion` = '{descripcion}', `fecha` = '{fecha}', `fecha` = '{hora}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deletePeliculasById(self, id):
        super().deleteRowById(id, self.tableName)


    
