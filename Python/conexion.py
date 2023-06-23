import mysql.connector

class MySQLConnection:
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            database=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa a MySQL")
        else:
            print("Error al conectar a MySQL")

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def cursor(self):
        return self.connection.cursor()
    
    def commit(self):
        self.connection.commit()
