from dx_logic import Logic
from boleto_obj import BoletoObj


class BoletoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "boleto"

    def getAllBoletos(self):
        boletoList = super().getAllRows(self.tableName)
        boletoObjList = []
        for element in boletoList:
            newBoleto = self.createBoletoObj(element)
            boletoObjList.append(newBoleto)
        return boletoObjList

    def createBoletoObj(
        self,
        idboleto,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        boletoObj = BoletoObj(
            id,
            tipo,
            fecha,
            hora,
            compradetallada_idcompra,
            sala_idsala,
            peliculas_idpeliculas,
        )
        return boletoObj

    def createBoletoObj(self, boletoDict):
        boletoObj = BoletoObj(
            boletoDict["tipo"],
            boletoDict["fecha"],
            boletoDict["hora"],
            boletoDict["compradetallada_idcompra"],
            boletoDict["sala_idsala"],
            boletoDict["peliculas_idpeliculas"],
            boletoDict["idboleto"],
        )
        return boletoObj

    def insertBoleto(
        self,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`boleto`(`idboleto`,`tipo`,`fecha`,`hora`, `compradetallada_idcompra`, `sala_idsala`, `peliculas_idpeliculas`) "
            + f"VALUES(0,'{tipo}','{fecha}','{hora}','{compradetallada_idcompra}','{sala_idsala}','{peliculas_idpeliculas}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateBoletoById(
        self,
        idboleto,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`boleto` "
            + f"SET `boleto` = '{tipo}','{fecha}','{hora}','{compradetallada_idcompra}','{sala_idsala}','{peliculas_idpeliculas}' "
            + f"WHERE `idboleto` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteBoletoById(self, idboleto):
        super().deleteRowById(id, self.tableName)
