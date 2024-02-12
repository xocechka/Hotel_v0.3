from django.db import models
from django.contrib.auth.models import User


class Habitacion(models.Model):
    tipo_habitacion={
        'independiente':'single',
        'boble':'double',
    }
    numero = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=50,choices=tipo_habitacion)
    precio_por_noche = models.IntegerField()
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='images')
    class Meta:
        db_table='habitacion'

class Trabajador(User):
    pass

class Administrador(User):
    
    def create(self,*args, **kwargs):
        self.is_staff=True
        

class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    habitaciones = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total=models.IntegerField()
    class Meta:
        db_table='reserva'

class Blog(models.Model):
    img=models.ImageField()
    descripcion=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='blog'