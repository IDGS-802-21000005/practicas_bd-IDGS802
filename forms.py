from wtforms import Form
from wtforms import StringField, TextAreaField,IntegerField, SelectField, RadioField
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