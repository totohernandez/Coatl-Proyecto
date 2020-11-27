from dx_logic import Logic
from compradetallada_obj import CompraDetObj


class CompraDetLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "compradetallada"

    def getAllCompras(self):
        compraList = super().getAllRows(self.tableName)
        compraObjList = []
        for element in compraList:
            newCompra = self.createCompraDetObj(element)
            compraObjList.append(newCompra)
        return compraObjList

    def createCompraDetObj(
        self, idcompra, tipo, precios_unitarios, cantidad, monto_total
    ):
        compraObj = CompraDetObj(id, tipo, precios_unitarios, cantidad, monto_total)
        return compraObj

    def createCompraObj(self, userDict):
        compraObj = CompraDetObj(
            userDict["tipo"],
            userDict["precios_unitarios"],
            userDict["cantidad"],
            userDict["monto_total"],
            userDict["idcompra"],
        )
        return compraObj

    def insertCompra(self, tipo, precios_unitarios, cantidad, monto_total):
        database = self.database
        sql = (
            f"INSERT INTO `cine`.`compradetallada`(`idcompra`,`tipo`,`precios_unitarios`,`cantidad`,`monto_total`) "
            + f"VALUES(0,'{tipo}','{precios_unitarios}','{cantidad}','{monto_total}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCompraById(
        self, idcompra, tipo, precios_unitarios, cantidad, monto_total
    ):
        database = self.database
        sql = (
            "UPDATE `cine`.`compradetallada` "
            + f"SET `compradetallada` = '{tipo}','{precios_unitarios}','{cantidad}','{monto_total}' "
            + f"WHERE `idcompra` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCompraById(self, idcompra):
        super().deleteRowById(id, self.tableName)
