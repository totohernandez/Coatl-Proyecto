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
            # newSucursal = self.createSucursalObj(
            #     element.nombre,
            #     element.departamento,
            #     element.direccion,
            #     element.usuario_idusuario,
            # )
            # sucursalObjList.append(newSucursal)
            sucursalObjList.append(element)
        return sucursalObjList

    # def createSucursalObj(
    #     self, idsucursal, nombre, departamento, direccion, usuario_idusuario
    # ):
    #     sucursalObj = sucursalObj(id, nombre, direccion, usuario_idusuario)
    #     return sucursalObj

    def createSucursalObj(self, nombre, departamento, direccion, usuario_idusuario):
        sucursalDict = dict(
            nombre=nombre,
            departamento=departamento,
            direccion=direccion,
            usuario_idusuario=usuario_idusuario,
        )
        # sucursalObj = SucursalObj(
        #     sucursalDict["nombre"],
        #     sucursalDict["departamento"],
        #     sucursalDict["direccion"],
        #     sucursalDict["usuario_idusuario"],
        # )
        # return sucursalObj
        return sucursalDict

    def insertSucursal(self, nombre, departamento, direccion, usuario_idusuario):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`sucursal`(`idsucursal`,`nombre`,`departamento`,`direccion`, `usuario_idusuario`) "
            + f"VALUES(0,'{nombre}','{departamento}','{direccion}','{usuario_idusuario}');"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateSucursalById(
        self, idsucursal, nombre, departamento, direccion, usuario_idusuario
    ):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`sucursal` "
            + f"SET `nombre` = '{nombre}', `departamento` = '{departamento}', `direccion` = '{direccion}', `usuario_idusuario` = {usuario_idusuario} "
            + f"WHERE `idsucursal` = {idsucursal};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getSucursalById(self, idsucursal):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`sucursal` " + f"where idsucursal ={idsucursal};"
        sucursalDict = database.executeQueryOneRow(sql)
        return sucursalDict

    def deleteSucursalById(self, idsucursal):
        database = self.database
        sql = "DELETE FROM `dbcine`.`sucursal` " + f"WHERE idsucursal = {idsucursal};"
        row = database.executeNonQueryRows(sql)
        return row
