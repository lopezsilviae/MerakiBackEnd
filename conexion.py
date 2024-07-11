# instalar pymysql -> pip install pymysql
# importar pymysql / SQLachemy / dbmysql
import pymysql

# conectar con el servidor MySQL
def conectarMySQLLocal():
    # datos sensibles -> variables de entorno
    # local
     host="localhost"
     user="root"
     clave=""
     db="meraki"

     return pymysql.connect(host=host,user=user,password=clave,database=db)

    # deploy -> Pythonanywhere
def conectarMySQL():
    # datos sensibles -> variables de entorno
    # local
     host="lopezsilviae.mysql.pythonanywhere-services.com"
     user="lopezsilviae"
     clave="jcs.2024"
     db="lopezsilviae$meraki"

     return pymysql.connect(host=host,user=user,password=clave,database=db)

    



    