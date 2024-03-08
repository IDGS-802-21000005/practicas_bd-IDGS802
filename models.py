from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class Maestros(db.Model):
    __tablename__='maestros'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(80))
    amaterno=db.Column(db.String(80))
    telefono=db.Column(db.String(50))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
class Alumnos(db.Model):
    __tablename__='alumnos'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(80))
    amaterno=db.Column(db.String(80))
    email=db.Column(db.String(50))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
    
class Venta(db.Model):
    __tablename__='ventas'
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    telefono=db.Column(db.String(80))
    fecha=db.Column(db.DateTime)
    total=db.Column(db.String(50))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
    
