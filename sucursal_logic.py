from dx_logic import Logic
from sucursal_obj import SucursalObj


class SucursalLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "sucursal"

    def getAllSucursales(self):
        sucursalList = super().getAllRows(self.tableName)
        sucursalObjList = []
        for element in sucursalList:
            newSucursal = self.createSucursalObj(element)
            sucursalObjList.append(newSucursal)
        return sucursalObjList

    def createSucursalObj(
        self, idsucursal, nombre, departamento, direccion, usuario_idusuario
    ):
        sucursalObj = sucursalObj(id, nombre, direccion, usuario_idusuario)
        return sucursalObj

    def createSucursalObj(self, sucursalDict):
        sucursalObj = SucursalObj(
            sucursalDict["nombre"],
            sucursalDict["departamento"],
            sucursalDict["direccion"],
            sucursalDict["usuario_idusuario"],
        )
        return sucursalObj

    def insertSucursal(self, nombre, departamento, direccion, usuario_idusuario):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`sucursal`(`idsucursal`,`nombre`,`departamento`,`direccion`, `usuario_idusuario`) "
            + f"VALUES(0,'{nombre}','{departamento}','{direccion}','{usuario_idusuario}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateSucursalById(self, nombre, departamento, direccion, usuario_idusuario):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`sucursal` "
            + f"SET `nombre` = '{nombre}', `departamento` = '{departamento}', `direccion` = '{direccion}', `usuario_idusuario` = '{usuario_idusuario}' "
            + f"WHERE `idsucursal` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteSucursalById(self, idsucursal):
        super().deleteRowById(id, self.tableName)
