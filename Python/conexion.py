import mysql.connector

# definimos una clase llamada DatabaseConnection que establece la conexión con la base de datos MySQL
class DatabaseConnection():

# constructor de la clase "init": El constructor de una clase es un método especial que se llama automáticamente cuando se crea una instancia de la clase. 
# Su propósito principal es inicializar los atributos de la instancia. 
# El método __init__ se utiliza como el constructor de la clase DatabaseConnection. 
# Recibe los parámetros host, user, password, port y database, que son los datos necesarios para establecer la conexión con la base de datos. 
# Dentro del constructor, estos parámetros se asignan a los atributos correspondientes de la instancia utilizando la sintaxis self.nombre_del_atributo = valor. 
# Esto asegura que los datos proporcionados al crear una instancia de DatabaseConnection se almacenen correctamente en los atributos de esa instancia.

us
    def __init__(self, host, user, password, port, database): 

# establecemos los atributos de la clase, datos necesarios para establecer la conexión
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.port = 3308
        self.database = 'novo_mundo'
        self.connection = None 
# Este valor inicial puede ser útil para verificar posteriormente si la conexión ha sido exitosa o no.

    def connect(self):
# se define el método connect dentro de la clase DatabaseConnection, que permite establecer la conexión con la base de datos MySQL utilizando los atributos de la instancia de la clase
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port, 
                database=self.database
            )
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as error:
# si ocurre algún error durante la conexión, se captura la excepción y se imprime un mensaje de error más descriptivo
            print("No se pudo establecer la conexión: {}".format(error))

# para verificar si la conexión ha sido establecida:
# La diferencia entre las dos formas de cómo manejan los errores al intentar establecer la conexión a la base de datos.
# SI utiliza try-except, se intenta establecer la conexión dentro del bloque try. 
# Si ocurre algún error durante la ejecución de ese código, se captura la excepción mysql.connector.Error en el bloque except. Esto permite capturar y manejar de manera específica cualquier error que pueda ocurrir durante la conexión. En este caso, se imprime un mensaje de error más descriptivo que incluye información sobre la excepción específica que se produjo.
# En cambio si se utiliza la estructura if-else, se verifica si la conexión está establecida utilizando el método is_connected() del objeto de conexión self.connection. Si la conexión está establecida, se imprime el mensaje "Conexión exitosa a la base de datos.". De lo contrario, se imprime el mensaje "No se pudo establecer la conexión.". Esta forma de verificación se basa en el estado de la conexión después de intentar establecerla, sin capturar y manejar específicamente los errores que puedan ocurrir durante el proceso. En resumen, la principal diferencia es que el enfoque try-except captura y maneja los errores específicos que pueden ocurrir durante la conexión, proporcionando mensajes de error más detallados. Mientras que el enfoque if-else simplemente verifica el estado de la conexión después de intentar establecerla, sin manejar los errores de manera específica. La elección entre ambos enfoques depende de tus necesidades y preferencias en cuanto al manejo de errores.

    def close(self):  #cerramos conexion
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")


connection = DatabaseConnection(
    host='localhost',
    user='root', 
    password='',
    port='3308',
    database='novo_mundo'
)
# Establecer la conexión
connection.connect()

# Cerrar la conexión
connection.close()
