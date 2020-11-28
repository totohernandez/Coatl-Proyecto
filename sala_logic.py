from dx_logic import Logic
from sala_obj import SalaObj


class SalaLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "sala"

    def getAllSalas(self):
        salaList = super().getAllRows(self.tableName)
        salaObjList = []
        for element in salaList:
            newSala = self.createSalaObj(element)
            salaObjList.append(newSala)
        return salaObjList

    def createSalaObj(self, idsala, capacidad, tipo):
        salaObj = SalaObj(id, capacidad, tipo)
        return salaObj

    def createSalabj(self, salaDict):
        salaObj = SalaObj(salaDict["capacidad"], salaDict["tipo"], salaDict["idsala"])
        return salaObj

    def insertAsiento(self, capacidad, tipo):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`sala`(`idsala`,`capacidad`,`tipo`)"
            + f"VALUES(0,'{capacidad}','{tipo});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateSalaById(self, idsala, capacidad, tipo):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`sala` "
            + f"SET `sala` = '{capacidad}','{tipo}'"
            + f"WHERE `idsala` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteAsientoById(self, idsala):
        super().deleteRowById(id, self.tableName)