import pymysql
from conexion import conectarMySQL


# consultar  Pedidos Pendientes
def obtenerPedidos():
    # conexion mysql
    conexion = conectarMySQL()
    pedidos = []
    with conexion.cursor() as cursor:
        # Create a new record
        sql = """SELECT * FROM pedidosproductos where estado='pedido'"""
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return pedidos

# consultar  Pedidos Realizados   
def obtenerPedidosRealizados():
    # conexion mysql
    conexion = conectarMySQL()
    pedidos = []
    with conexion.cursor() as cursor:
        # Create a new record
        sql = """SELECT * FROM pedidosproductos where estado='realizado'"""
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return pedidos

# Insertar
def registrarPedido(cliente,correo,cel,calle,cp,imagen,cantidad_prod):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT  pedidosproductos (nombre_solicitante,email,telefono,direccion,cp,producto,cantidad) VALUES (%s, %s, %s,%s, %s, %s, %s)"
        cursor.execute(query,(cliente,correo,cel,calle,cp,imagen,cantidad_prod))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
    

# Update 1) ubicar por id el producto a modificar
def obtenerPedidoId(id):
    conexion = conectarMySQL()
    pedido = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM pedidosproductos WHERE id = %s", (id,))
        pedido = cursor.fetchone()
    conexion.close()
    return pedido

# 2) Actualizar el estado del pedido
def ActualizarEstadoPedido( estado,cantidadProducto, id):

    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE pedidosproductos SET estado = %s, cantidad = %s WHERE id = %s",(estado,cantidadProducto, id))

        result = cursor
    conexion.commit()
    conexion.close()
    return result

# Borrar pedidos que no se van a realizar
def eliminarPedido(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM pedidosproductos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result