
import mysql.connector

from mysql.connector import errorcode

#Hola chicos hoy no van a tener texto afuera, vamos a trabajar aca directamente,
#probablemente yo este en unas charlas toda la mañana asi que necesito que presten atencion para que puedan ir avanzando
#este codigo que arme es una conexion a base de datos simple, para una base de datos que les creo sofi
#les voy a dejar el codigo abajo para crear la tabla para que puedan practicar
#les recomiendo que practiquen con este codigo primero y luego van a hacer unos ejercicios con esto
#primero lo primero no se olviden de abrir el Xammp y abrir la base de datos en el workbench sino no va a funcionar
# y tambien copien el codigo para crear las tablas que les dio sofi
# recuerden sofi no les creo la base de datos como tal sino la ejecucion para que tengan todas las tablas armadas

#---------------------------------------------------------------------------------------------------------------------#

#empezemos, si me dieron bola en general tiene una idea de lo que son las variables globales y el pasaje de datos
#para este ejemplo y para la simplicidad general del codigo vamos a crear dos variables globales, una llamada cursor
# y una llamada conexion y les vamos a poner valores nulos


cursor = None
cnx = None

#vamos a separar de manera prolija nuestro codigo en diferentes funciones, siendo la primera la conexion con la base de
#datos

def ConectarBase():
    # lo primeros que hacemos es poner global a nuestras variables, esto significa que no solo va a usar las variables
    #globales sino que cuando estas variables las cambie esta porcion del codigo tambien van a guardarse globalmente
    global cnx, cursor

    #una vez hecho esto abrimos una estructura try except, ya que la conexion puede fallar por muchos factores y no
    # queremos que nuestro codigo pare
    try:
        #vamos a instanciar que nuestra variable va a ser igual a lo que devuelva el metodo connect
        #este puede recibir mucho valores, nosotros tenemos que decirle que valor es y el valor como tal
        #vamos a estructurarlo de la siguiente manera, usuario, contraseña, host y nombre de la base
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="basededatosconnection20")
        # cursor es la variable con la que nos vamos a referir a las lineas de consulta que les vamos a mandar
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')

    #luego hacemos un except con los errores
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)
#una vez hecho esa parte del codigo, vamos a tener esas 2 variables prontas para usar
#lo siguiente es hacer las consultas que es la parte mas facil
#solamente instanciamos un string con la consulta adentro
#y luego ponemos cursor.execute(consulta)
# si queremos guardar el valor le decimos que queremos metodo fetchall() del cursor
#esto nos va a devolver todas las filas de la consulta que se ejecuto
#esto  NO CAMBIA NADA DE LA BASE DE DATOS, para que lo haga tenemos que poner conexion.commit
#pero para hacer un select no necesitamos cambiar nada de la base de datos
def ConsultaSelect():
    Consulta = "SELECT * FROM alumnos;"
    cursor.execute(Consulta)
    return cursor.fetchall()

#para insertar es la misma tarea, pero vamos a cambiar un poco como hacemos las consultas que comunmente hacemos
#hay muchas formas en las que pueden vulnerar nuestras base de datos, una de ellas es añadiendo codigo a nuestras
#consultas, para evitar esto, jamas tenemos que escribir nuestras consultas enteras
#tenemos que hacer consultas parametrizadas, lo que significa que cada valor va a ser un parametro, que luego nosotros
#enviamos cuando ejecutamos el metodo execute
#traduciendolo a python lo que tenemos que hacer es poner %s en cada valor de la consulta en vez de poner el valor
#luego cuando ejecutamos cursor.execute le pasamos como parametro no solo la consulta si no tambien el valor de los
#datos en orden
#en este caso los datos se los pasamos cuando ejecutamos la funcion y deberian de estructurarlo asi siempre

def ConsultaInsertar(nombre,edad,año,correo):
    sql = "INSERT INTO alumnos (nombre, edad, año, correo)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql,(nombre,edad,año,correo))
    cnx.commit()
    return cursor.lastrowid

#una vez hechas ambas funciones vamos a ejecutar la conexion de la base de datos y luego vamos a ejecutar la funcion
#insertar para que inserte lo que queremos a la tabla
#luego vamos a imprimir lo que devuelve ConsultaSelect para ver si se ejecuto de manera correcta

ConectarBase()
ConsultaInsertar("demian", 17, 4, "demian.correaet32@gmail.com")
print(ConsultaSelect())
#por ulitmo vamos a cerrar la base de datos, lo cual es extremadamente importante y no nos tenemos que olvidar
if cnx.is_connected():
    cnx.close()
    print("La conexión a la base de datos ha sido cerrada.")
#recuerden que lo que devuelve la base de datos es un diccionario o una lista de diccionarios, asi que a partir
#de ahi trabajan como normalmente trabajarian con la base de datos
#les voy a dejar unos ejercicios que van a usar esta base de datos, intenten estructuralos en diferente funciones
#dentro de este mismo codigo
