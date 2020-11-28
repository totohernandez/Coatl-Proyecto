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
        self, idcompra, tipo, precios_unitarios, cantidad, monto_total, estado
    ):
        compraObj = CompraDetObj(
            id, tipo, precios_unitarios, cantidad, monto_total, estado
        )
        return compraObj

    def createCompraObj(self, compraDict):
        compraObj = CompraDetObj(
            compraDict["tipo"],
            compraDict["precios_unitarios"],
            compraDict["cantidad"],
            compraDict["monto_total"],
            compraDict["idcompra"],
            compraDict["estado"],
        )
        return compraObj

    def insertCompra(self, tipo, precios_unitarios, cantidad, monto_total, estado):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`compradetallada`(`idcompra`,`tipo`,`precios_unitarios`,`cantidad`,`monto_total`,`estado`) "
            + f"VALUES(0,'{tipo}','{precios_unitarios}','{cantidad}','{monto_total}'',{estado}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCompraById(
        self, idcompra, tipo, precios_unitarios, cantidad, monto_total, estado
    ):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`compradetallada` "
            + f"SET `compradetallada` = '{tipo}','{precios_unitarios}','{cantidad}','{monto_total}',{estado}' "
            + f"WHERE `idcompra` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCompraById(self, idcompra):
        super().deleteRowById(id, self.tableName)
