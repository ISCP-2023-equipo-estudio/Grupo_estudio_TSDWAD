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

    def insertarNuevaNormativa(self, idTipoNormativa, nroNormativa, fecha, descripcion, categoria, idTipoJurisdiccion, palabrasClave):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        sql = "INSERT INTO normativa(idTipoNormativa, fecha, descripcion, palabrasClaves, idTipoJurisdiccion, nroNormativa, idCategoria) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(idTipoNormativa, fecha, descripcion, palabrasClave, idTipoJurisdiccion, nroNormativa, categoria))
        self.conexion.commit()
        cursor.close()
        self.conexion.close()

    def consultarNormativas(self):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM normativa")
        normativas = cursor.fetchall()
        y=0
        x=0
        for i in normativas:
            linea= ""
            for x in range (8):
                linea += str(normativas[y][x]) + "  |  "
            y+=1
            print(linea)
        return
    
    def  obtenerNormativaPorNroNormativa(self,nroNormativa):
        self.conexion.connect()
        cursor=self.conexion.cursor()
        cursor.execute("SELECT * FROM normativa WHERE nroNormativa=%s" , (nroNormativa,) ) 
        normativas=cursor.fetchall() 
        y=0
        x=0
        for i in normativas:
            linea= ""
            for x in range (8):
                linea += str(normativas[y][x]) + "  |  "
            y+=1
            print(linea)
        return



    def eliminarNormativa(self, nroRegistro):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM normativa WHERE nroRegistro=%s", (nroRegistro,))
        self.conexion.commit()
        print("Fue eliminado exitosamente")

    
    def buscar_pclave(self, palabras_clave):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        query = "SELECT * FROM normativa WHERE "
        conditions = []
        for palabra in palabras_clave:
            conditions.append("LOWER(palabasClaves) LIKE '%{}%'".format(palabra))
        query += " OR ".join(conditions)
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    def obtenerCategorias(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * from categoria")
        categorias = cursor.fetchall()
        y=0
        x=0
        for i in categorias:
            for x in range (2):
                print(categorias[y][x])
            y+=1
        return
    
    def obtenerJurisdicciones(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * from tipoJurisdiccion")
        jurisdicciones = cursor.fetchall()
        y=0
        x=0
        for i in jurisdicciones:
            for x in range (2):
                print(jurisdicciones[y][x])
            y+=1
        return
    
    
