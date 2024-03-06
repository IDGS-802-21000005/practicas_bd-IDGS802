from wtforms import Form
from wtforms import StringField, TextAreaField,IntegerField, SelectField, RadioField, BooleanField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("id")
    nombre=StringField("nombre",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4, max=10, message='ingresa nombre valido')])
    apaterno=StringField("apaterno")
    amaterno=StringField("amaterno")
    telefono=IntegerField("telefono")
    email=EmailField("correo",[validators.Email(message='Ingresa un correo valido')])   
    
class PizzaForm(Form):
    nombre=StringField("Nombre",[validators.DataRequired(message='Nombre requerido'),
                                 validators.length(min=3, max=30, message='Minimo 3 caracteres y maximo 30 caracteres')])
    direccion=StringField("Dirección",[validators.DataRequired(message='Direccion requerida'),
                                 validators.length(min=3, max=30, message='Minimo 3 caracteres y maximo 30 caracteres')])
    telefono=StringField("Teléfono",[validators.DataRequired(message='Telefono requerido'),
                                 validators.length(min=10, max=20, message='Minimo 10 caracteres y maximo 20 caracteres')])
    num_pizzas=IntegerField("Número de pizzas",[validators.DataRequired(message='Numero requerido'),
                                 validators.NumberRange(min=1, max=20, message='Minimo una pizza maximo 20 pizzas')])
    champinion=BooleanField('Champiñones $10')
    pinia=BooleanField('Piña $10')
    jamon=BooleanField('Jamón $10')
    tamano= RadioField('Tamaño',choices=[('Chica','Chica $40'),('Mediana','Mediana $80'),('Grande','Grande $120')],validators=[validators.DataRequired(message='Tamaño requerido')])

class VentaForm(Form):
    dia=StringField("Dia",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=1, max=2, message='ingresa dia valido')])
    mes=StringField("Mes",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=1, max=2, message='ingresa mes valido')])
    anio=StringField("Año",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4, max=4, message='ingresa año valido')])
    formato= RadioField('Formato',choices=[('m','Mes'),('d','Dia')],validators=[validators.DataRequired(message='el campo es requerido')])