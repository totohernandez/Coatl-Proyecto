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
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        boletoObj = BoletoObj(
            id,
            fecha,
            hora,
            compradetallada_idcompra,
            sala_idsala,
            peliculas_idpeliculas,
        )
        return boletoObj

    def createBoletoObj(self, userDict):
        boletoObj = BoletoObj(
            userDict["fecha"],
            userDict["hora"],
            userDict["compradetallada_idcompra"],
            userDict["sala_idsala"],
            userDict["peliculas_idpeliculas"],
            userDict["idboleto"],
        )
        return boletoObj

    def insertBoleto(
        self, fecha, hora, compradetallada_idcompra, sala_idsala, peliculas_idpeliculas
    ):
        database = self.database
        sql = (
            f"INSERT INTO `cine`.`boleto`(`idboleto`,`fecha`,`hora`, `compradetallada_idcompra`, `sala_idsala`, `peliculas_idpeliculas`) "
            + f"VALUES(0,'{fecha}','{hora}','{compradetallada_idcompra}','{sala_idsala}','{peliculas_idpeliculas}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateBoletoById(
        self,
        idboleto,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
    ):
        database = self.database
        sql = (
            "UPDATE `cine`.`boleto` "
            + f"SET `boleto` = '{fecha}','{hora}','{compradetallada_idcompra}','{sala_idsala}','{peliculas_idpeliculas}' "
            + f"WHERE `idboleto` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteBoletoById(self, idboleto):
        super().deleteRowById(id, self.tableName)
