from rest_framework import serializers
from .models import User,Habitacion,Reserva,Blog
#from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        #permissions_classes=[IsAuthenticated]
        
class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['id', 'numero', 'tipo', 'precio_por_noche', 'disponible', 'descripcion', 'imagen']

class ReservaSerializer(serializers.ModelSerializer):
    habitaciones = HabitacionSerializer()  
    cliente = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  
    class Meta:
        model = Reserva
        fields = ['id', 'cliente', 'habitaciones', 'fecha_inicio', 'fecha_fin', 'precio_total']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'img', 'descripcion', 'fecha_creacion']
