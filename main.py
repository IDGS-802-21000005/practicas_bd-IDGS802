from flask import Flask, request,render_template, Response

from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash
from config import DevelopmentConfig
from models import db
from models import Alumnos, Maestros
import forms
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

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

    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()