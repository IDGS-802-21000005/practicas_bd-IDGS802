from flask import Flask, request,render_template, Response, redirect, url_for

from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash, jsonify
from config import DevelopmentConfig
from models import db

from models import Alumnos, Maestros, Venta
import forms
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

from datetime import datetime, timedelta
from pizzas import PizzaManager

@app.route("/", methods=["GET","POST"])
def index():
    pizza_form=forms.PizzaForm(request.form)
    pizza_form3=forms.VentaForm(request.form)
    ventas=Venta.query.filter(Venta.fecha.cast(db.Date) == datetime.now().date()).all()
    pizzas = pizza_manager.obtener_pizzas()
    flash("Ventas de hoy")
    return render_template("pizzas.html",  form1=pizza_form, form3=pizza_form3, pizzas=pizzas, ventas=ventas)

@app.route("/insertar/alumnos", methods=["GET","POST"])
def alumnos():
    alumnos_form=forms.UserForm(request.form)
    
    if request.method == "POST" and alumnos_form.validate():
        alum=Alumnos(nombre=alumnos_form.nombre.data,
                    apaterno=alumnos_form.apaterno.data,
                    email=alumnos_form.email.data)
        #insert into alumnos values()
        db.session.add(alum)
        db.session.commit()
        
    return render_template("insertar_alumnos.html", form=alumnos_form)

@app.route("/insertar/maestros", methods=["GET","POST"])
def maestros():
    maestros_form=forms.UserForm(request.form)
    
    if request.method == "POST" and maestros_form.validate():
        mast=Maestros(nombre=maestros_form.nombre.data,
                    apaterno=maestros_form.apaterno.data,
                    amaterno=maestros_form.amaterno.data,
                    telefono=maestros_form.telefono.data,
                    email=maestros_form.email.data)
        #insert into alumnos values()
        db.session.add(mast)
        db.session.commit()
        
    return render_template("insertar_maestros.html", form=maestros_form)

@app.route("/ver/alumnos", methods=["GET","POST"])
def ver_alumnos():
    alumnos=Alumnos.query.all()
    return render_template("ver_alumnos.html", alumnos=alumnos) 

@app.route("/ver/maestros", methods=["GET","POST"])
def ver_maestros():
    maestros=Maestros.query.all()
    return render_template("ver_maestros.html", maestros=maestros) 

@app.route("/eliminar/alumnos",methods=["GET","POST"])
def eliminar_alumnos():
    alumnos_form=forms.UserForm(request.form)
    if request.method == "GET":
        id=request.args.get("id")
        alum1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alumnos_form.id.data=alum1.id
        alumnos_form.nombre.data=alum1.nombre
        alumnos_form.apaterno.data=alum1.apaterno
        alumnos_form.email.data=alum1.email
    if request.method == "POST":
        id=alumnos_form.id.data
        alum=Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for("/ver/alumnos"))
    return render_template("eliminar_alumnos.html", form=alumnos_form)

@app.route("/eliminar/maestros",methods=["GET","POST"])
def eliminar_maestros():
    maestros_form=forms.UserForm(request.form)
    if request.method == "GET":
        id=request.args.get("id")
        mast1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
        maestros_form.id.data=mast1.id
        maestros_form.nombre.data=mast1.nombre
        maestros_form.apaterno.data=mast1.apaterno
        maestros_form.email.data=mast1.email
    if request.method == "POST":
        id=maestros_form.id.data
        mast=Alumnos.query.get(id)
        db.session.delete(mast)
        db.session.commit()
        return redirect(url_for("/ver/alumnos"))
    return render_template("eliminar_alumnos.html", form=maestros_form)
    
pizza_manager = PizzaManager()

@app.route("/pizza/agregar",methods=["GET","POST"])
def pizza_agregar():
    
    pizza_form=forms.PizzaForm(request.form)
    pizza_form3=forms.VentaForm(request.form)
    
    if request.method == "POST" and pizza_form.validate():
        nombre=pizza_form.nombre.data
        direccion=pizza_form.direccion.data
        telefono=pizza_form.telefono.data
        
        num_pizzas=pizza_form.num_pizzas.data
        champinion=pizza_form.champinion.data
        champinion=("Champiñones" if champinion else "")
        pinia=pizza_form.pinia.data
        pinia=("Piña" if pinia else "")
        jamon=pizza_form.jamon.data
        jamon=("Jamón" if jamon else "")
        tamano=pizza_form.tamano.data
        
        ingredientes = ','.join([ingrediente for ingrediente in [champinion, pinia, jamon] if ingrediente])
        
        pizza_manager.agregar_pizza(nombre,direccion,telefono,ingredientes, tamano, num_pizzas)
    ventas=Venta.query.filter(Venta.fecha.cast(db.Date) == datetime.now().date()).all()
    pizzas = pizza_manager.obtener_pizzas()
    flash("Ventas de hoy")
    return render_template("pizzas.html",  form1=pizza_form, form3=pizza_form3, pizzas=pizzas, ventas=ventas)

@app.route("/pizza/eliminar",methods=["GET","POST"])
def pizza_eliminar():
    
    if request.method == "POST":
        pizza_manager.eliminar_pizza(int(request.form["id"]))
    
    return redirect(url_for("pizza_agregar"))

@app.route("/pizza/cancelar",methods=["GET","POST"])
def pizza_cancelar():
    
    if request.method == "POST":
        pizza_manager.eliminar_pizzas()
    
    return redirect(url_for("pizza_agregar"))
    
@app.route("/ventas/finalizar",methods=["GET","POST"])
def ventas_finalizar():
    pizza_form=forms.PizzaForm(request.form)
    pizza_form3=forms.VentaForm(request.form)

    if request.method == "POST":
        
        cliente = pizza_manager.obtener_cliente()
        
        total = pizza_manager.total()
        
        venta = Venta(nombre=cliente["nombre"], direccion=cliente["direccion"], telefono=cliente["telefono"], fecha=datetime.now(), total=total)
                    
        db.session.add(venta)
        db.session.commit()
        pizza_manager.eliminar_pizzas()
    pizzas = pizza_manager.obtener_pizzas()
    ventas=Venta.query.filter(Venta.fecha.cast(db.Date) == datetime.now().date()).all()
    flash("Ventas de hoy")
    return render_template("pizzas.html",  form1=pizza_form, form3=pizza_form3, pizzas=pizzas, ventas=ventas)

@app.route("/ventas/buscar",methods=["GET","POST"])
def ventas_buscar():
    pizza_form=forms.PizzaForm(request.form)
    pizza_form3=forms.VentaForm(request.form)
    
    if request.method == "POST" and pizza_form3.validate():
        dia=pizza_form3.dia.data
        mes=pizza_form3.mes.data
        anio=pizza_form3.anio.data
        formato=pizza_form3.formato.data
        ventas = []
        if formato == 'd':
            ventas=Venta.query.filter(Venta.fecha.cast(db.Date) == datetime(int(anio),int(mes),int(dia))).all()
            flash(f"Ventas de {dia}/{mes}/{anio}")
        elif formato == 'm':
            fecha_inicio = datetime(year=int(anio), month=int(mes), day=1)
            # Calcular el último día del mes
            fecha_fin = datetime(year=int(anio), month=int(mes)+1, day=1) - timedelta(days=1)
            
            # Filtrar las ventas por el rango de fechas
            ventas = Venta.query.filter(Venta.fecha >= fecha_inicio, Venta.fecha <= fecha_fin).all()
            flash(f"Ventas de {mes}/{anio}")
        
        pizzas = pizza_manager.obtener_pizzas()
        return render_template("pizzas.html",  form1=pizza_form, form3=pizza_form3, pizzas=pizzas, ventas=ventas)
    
    ventas=Venta.query.filter(Venta.fecha.cast(db.Date) == datetime.now().date()).all()
    flash("Ventas de hoy")
    pizzas = pizza_manager.obtener_pizzas()
    return render_template("pizzas.html",  form1=pizza_form, form3=pizza_form3, pizzas=pizzas, ventas=ventas)
 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=4000)
    