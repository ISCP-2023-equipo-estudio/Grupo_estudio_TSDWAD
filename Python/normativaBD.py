import mysql.connector
from conexion import *


class NormativaBD():
    def __init__(self):
        #self.conexion = mysql.connector.connect(host="localhost", user="root", passwd="admin", database="bdnormativas")
        self.conexion = MySQLConnection("localhost","root","admin", "bdnormativas")

    def obtenerTipoNormativa(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM TipoNormativa")
        tipoNormativas = cursor.fetchall()
        y=0
        x=0
        for i in tipoNormativas:
            print(tipoNormativas[y][0], tipoNormativas[y][1])
            y+=1
        self.conexion.close()

    def insertarNuevaNormativa(self, idTipoNormativa, nroNormativa, fecha, descripcion, categoria, idTipoJurisdiccion, idOrganoLegislativo, palabrasClave):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO normativa (nroNormativa,) VALUES (?,?,?,?,?,?,?)",(idTipoNormativa, nroNormativa, fecha,descripcion,categoria,idTipoJurisdiccion, idOrganoLegislativo,palabrasClave))
        self.conexion.close()

    def consultarNormativa(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM normativas")
        normativas = cursor.fetchall()
        y=0
        x=0
        for i in normativas:
            for x in range (9):
                print(normativas[y][x])
            y+=1
        return

    def eliminarNormativa(self, nroRegistro):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM normativa WHERE codigo=?", (nroRegistro))
        print("Fue eliminado exitosamente")