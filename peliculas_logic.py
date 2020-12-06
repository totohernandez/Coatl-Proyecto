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

    def createPeliculasObj(self, idpeliculas, titulo, descripcion, fecha, hora):
        peliculasObj = PeliculasObj(id, titulo, descripcion, fecha, hora)
        return peliculasObj

    def createPeliculasObj(self, peliculasDict):
        peliculasObj = PeliculasObj(
            peliculasDict["titulo"],
            peliculasDict["descripcion"],
            peliculasDict["fecha"],
            peliculasDict["hora"],
            peliculasDict["idpeliculas"],
        )
        return peliculasObj

    def insertPeliculas(self, titulo, descripcion, fecha, hora):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`peliculas`(`idpeliculas`,`titulo`,`descripcion`,`fecha`, `hora`) "
            + f"VALUES(0,'{titulo}','{descripcion}','{fecha}','{hora}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updatePeliculasById(self, titulo, descripcion, fecha, hora):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`peliculas` "
            + f"SET `titulo` = '{titulo}', `descripcion` = '{descripcion}', `fecha` = '{fecha}', `fecha` = '{hora}' "
            + f"WHERE `idpeliculas` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deletePeliculasById(self, idpeliculas):
        super().deleteRowById(id, self.tableName)
