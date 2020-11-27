from dx_logic import Logic
from sucursal_obj import SucursalObj


class SucursalLogic(Logic):
    def __init__(self):
        super().__init__()

    def getAllSucursales(self):
        sucursalList = super().getAllRows(self.tableName)
        sucursalObjList = []
        for element in sucursalList:
            newSucursal = self.createSucursalObj(element)
            sucursalObjList.append(newSucursal)
        return sucursalObjList

    def createSucursalObj(self, id, nombre, departamento, direccion, usuario_idusuario):
        sucursalObj = sucursalObj(id, nombre, direccion, usuario_idusuario)
        return sucursalObj
    
    def createSucursalObj(self, userDict):
        sucursalObj = SucursalObj(
            userDict["nombre"],
            userDict["departamento"],
            userDict["direccion"],
            userDict["usuario_idusuario"],
        )
        return sucursalObj

    def insertSucursal(self, nombre, departamento, direccion, usuario_idusuario):
        database = self.database
        sql = (
            f"INSERT INTO `cine`.`sucursal`(`id`,`nombre`,`departamento`,`direccion`, `usuario_idusuario`) "
            + f"VALUES(0,'{nombre}','{departamento}','{direccion}','{usuario_idusuario}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateSucursalById(self, nombre, departamento, direccion, usuario_idusuario):
        database = self.database
        sql = (
            "UPDATE `cine`.`sucursal` "
            + f"SET `nombre` = '{nombre}', `departamento` = '{departamento}', `direccion` = '{direccion}', `usuario_idusuario` = '{usuario_idusuario}' "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteSucursalById(self, id):
        super().deleteRowById(id, self.tableName)


    


