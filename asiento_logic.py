from dx_logic import Logic
from asiento_obj import AsientoObj


class AsientoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "asiento"

    def getAllAsientos(self):
        asientoList = super().getAllRows(self.tableName)
        asientoObjList = []
        for element in asientoList:
            newAsiento = self.createAsientoObj(element)
            asientoObjList.append(newAsiento)
        return asientoObjList

    def createAsientoObj(self, idasiento, silla_numero, fila_letras):
        asientoObj = AsientoObj(id, silla_numero, fila_letras)
        return asientoObj

    def createAsientoObj(self, userDict):
        asientoObj = AsientoObj(userDict["silla_numero"], userDict["fila_letras"])
        return asientoObj

    def insertAsiento(self, silla_numero, fila_letras):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`asiento`(`idasiento`,`silla_numero`,`fila_letras`)"
            + f"VALUES(0,'{silla_numero}','{fila_letras});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateAsientoById(self, idasiento, silla_numero, fila_letras):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`asiento` "
            + f"SET `asiento` = '{silla_numero}','{fila_letras}'"
            + f"WHERE `idasiento` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteAsientoById(self, idasiento):
        super().deleteRowById(id, self.tableName)
