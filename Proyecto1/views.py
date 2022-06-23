import datetime
from datetime import date, datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse ("<br><br>Ya entendimos esto, es muy simple ;)")

def diaDeHoy(request):

    dia = datetime.now()

    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse (documentoDeTexto)

def tercera_vista(request, fecha):
    fecha_actual = date.today()
    anio = fecha_actual.year
    fecha = int(fecha)
    resultado = anio - fecha
    retorno = f"El año en que naciste es : {resultado}"
    return HttpResponse(retorno)    

""" def probandoTemplate(self):

    nom = "Bruno"
    ap = "Monassa"

    listaDeNotas = [2,2,4,5,6,7]

    diccionario = {"nombre" :nom, "apellido":ap, "hoy":date.today(), "notas":listaDeNotas}

    miHtml = open("C:/Users/Brunito/Desktop/PythonProyecto1/Proyecto1/Proyecto1/plantilla/template1.html")

    plantilla = Template(miHtml.read())

    miHtml.close()
    
    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento) """

def probandoTemplate(self):

    nom = "Bruno"
    ap = "Monassa"

    listaDeNotas = [2,2,4,5,6,7]

    diccionario = {"nombre" :nom, "apellido":ap, "hoy":date.today(), "notas":listaDeNotas}

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
