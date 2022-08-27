from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from familiares_app.models import Hijos, Padres, Hermanos
import datetime

# Create your views here.

def add_padre(request):
    
    padre = Padres(nombre="Leandro",
                   telefono=351000000,
                   nacimiento=datetime.date(1927, 1, 6),
                   email='leandro@gmail.com')
    
    madre = Padres(nombre="Martha",
                   telefono=351111111,
                   nacimiento=datetime.date(1926, 8, 14),
                   email='martha@gmail.com')
    
    padre.save()
    madre.save()
    
    diccionario = {"nombre_p" : padre.nombre, "telefono_p" : padre.telefono,
                   "nacimiento_p" : padre.nacimiento, "email_p" : padre.email,
                   "nombre_m" : madre.nombre, "telefono_m" : madre.telefono,
                   "nacimiento_m" : madre.nacimiento, "email_m" : madre.email,}
    
    plantilla = loader.get_template("padres.html")
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


def add_hijo(request):
    
    hijo = Hijos(nombre="Cristian",
                 telefono=351000000,
                 nacimiento=datetime.date(1986, 7, 11),
                 email='cristian@gmail.com')
    
    hija = Hijos(nombre="Romina",
                 telefono=351111111,
                 nacimiento=datetime.date(1988, 6, 12),
                 email='romina@gmail.com')
    
    hijo.save()
    hija.save()
    
    diccionario = {"nombre_o" : hijo.nombre, "telefono_o" : hijo.telefono,
                   "nacimiento_o" : hijo.nacimiento, "email_o" : hijo.email,
                   "nombre_a" : hija.nombre, "telefono_a" : hija.telefono,
                   "nacimiento_a" : hija.nacimiento, "email_a" : hija.email,}
    
    plantilla = loader.get_template("hijos.html")
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


def add_hermano(request):
    
    hermano = Hermanos(nombre="Leandro",
                       telefono=351000000,
                       nacimiento=datetime.date(1960, 5, 10),
                       email='leandro@gmail.com')
    
    hermana = Hermanos(nombre="Fabiana",
                       telefono=351111111,
                       nacimiento=datetime.date(1966, 7, 24),
                       email='fabiana@gmail.com')
    
    hermano.save()
    hermana.save()
    
    diccionario = {"nombre_o" : hermano.nombre, "telefono_o" : hermano.telefono,
                   "nacimiento_o" : hermano.nacimiento, "email_o" : hermano.email,
                   "nombre_a" : hermana.nombre, "telefono_a" : hermana.telefono,
                   "nacimiento_a" : hermana.nacimiento, "email_a" : hermana.email,}
    
    plantilla = loader.get_template("hermanos.html")
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)