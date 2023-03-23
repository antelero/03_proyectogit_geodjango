from django.db import models
from django_currentuser.middleware import get_current_authenticated_user
# Create your models here.
from datetime import datetime

 class Model(models.Model):
    tipo_inmueble  = models.CharField(max_length=200) #Tipologia
    ubicacion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    dptopartida= models.CharField(max_length=9)
   
    #relevamiento
    fuente_informacion = models.CharField(max_length=250)
    tipo_de_valor
    oferta_publicada
    valor_total 
    valor_por_M2
    moneda
    fecha_relevamiento 

    superficie_Lote
    unidad_Lote
    situacion_juridica #escritura boleto derechos posesorios*
    frente
    forma
    ubicacion #Cuadra o esquina
    tipo_de_barrio #abierto cerrado country

    #Servicios
    luz = models.BooleanField()
    agua= models.BooleanField()
    gas_natural = models.BooleanField()
    cloacas= models.BooleanField()
    pavimento = models.BooleanField()
    cordon_cuneta = models.BooleanField()
    observaciones = models.CharField(max_length=250)

    date_created = models.DateTimeField() #Fecha de Carga
    date_modified = models.DateTimeField()

 def save(self):
    if self.date_created == None:
       self.date_created = datetime.now()
    self.date_modified = datetime.now()
    super(Model, self).save()



Tipo de Valor *
Oferta Publicada
Valor Total *
4.500.000
Valor por M2 *
valor por metro cuadrado
Tipo de Moneda *
Dólares
Fecha del Valor *
04/2022
Superficie Lote (m2) *
76.812
Situación Jurídica *
Con escritura
Frente *
273,00
Forma *
Regular
Topografía *
Llano
Ubicación Cuadra
Esquina
Tipo de Barrio *
Abierto
Luz *
Sin Datos
Agua *
Sin Datos
Gas natural *
Sin Datos
Cloacas *
Sin Datos
Pavimento *
Pavimentado
Cordón Cuneta *
Sin Cordón Cuneta
Observaciones
Ubicado Av. Japón entre Av. Juan B Justo y Av. Rancagua.
Apto: viviendas, industrial, agrícola.
Archivos
Cargar
No se eligió ningún archivo
Drag & Drop.

D16Z12M001P005.png

chat.jpg
