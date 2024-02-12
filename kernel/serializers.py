from rest_framework import serializers
from .models import User,Habitacion,Reserva,Blog
#from rest_framework.permissions import IsAuthenticated

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password']
        #permissions_classes=[IsAuthenticated]

from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=['username','password']

class HabitacionSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(allow_empty_file=False, use_url=True)
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
