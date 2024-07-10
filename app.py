from flask import Flask, render_template, request, redirect
from negocioBD import  *
app = Flask(__name__)

@app.route("/")
def helloWorld():
    return render_template("index.html")

@app.route('/contacto')
def cargarContacto():
   title="contacto en china"
   return render_template("contacto.html")

@app.route('/nosotros')
def cargarNosotros():
   return render_template("nosotros.html")

@app.route('/servicios')
def cargarServicio():
    return render_template("servicios.html")
    
@app.route('/stock')
def cargarStock():
    return render_template("stock.html")


#funciones que manejan la base de datos#

@app.route("/listarPedidos")
def cargarPedidos():
    title = "Pedidos Meraki"
    pedidos = obtenerPedidos()
    return render_template("pedidos.html", pedidos=pedidos)

@app.route("/listarPedidosRealizados")
def cargarPedidosRealizados():
    title = "Pedidos Meraki"
    pedidos = obtenerPedidosRealizados()
    return render_template("pedidosRealizados.html", pedidos=pedidos)
    
@app.route('/cargarPedido')
def cargaPedido():
    title= "Solicitar Producto"
    return render_template("compras.html")    

@app.route("/insertarPedido", methods=['POST'])
def insertaPedido():
    print(request.form)
    cliente = request.form['nombre']
    correo = request.form['email']
    cel = request.form['telefono']
    calle = request.form['direccion']
    cp = request.form['codpostal']
    producto = request.form['imagen']
    cantProducto=request.form['cantidad_prod']
    result = registrarPedido(cliente,correo,cel,calle,cp,producto,cantProducto)
    print(result)
    return redirect("/")

@app.route('/borrarPedido/<int:id>')
def borrarPedido(id):
    eliminarPedido(id)
    return redirect("/listarPedidos")

# Actualizar el estado del producto
@app.route("/editarPedido/<int:id>")
def editarPedido(id):

    pedido = obtenerPedidoId(id)

    return render_template("comprasEdit.html",  pedido=pedido)

@app.route("/actualizarPedido", methods=['POST'])
def actualizarPedido():
    idPedido = request.form['pedido_id']
    estado = request.form['estado']
    cantidadProd = request.form['cantidad_prod']
    if (estado == ""):
        estado="pedido"

 
    ActualizarEstadoPedido(estado,cantidadProd,idPedido)
    return redirect("/listarPedidos")
 

