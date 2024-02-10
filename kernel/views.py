from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import HabitacionSerializer
from .models import Habitacion
from rest_framework.response import Response
from rest_framework import status

#User
class UserList(APIView):
    pass
class UserDetail(APIView):
    pass

#Habitacion
class HabitacionList(APIView):
    def list_habitacion(self,request):
        try:
           habitaciones=Habitacion.objects.all()
           serializer=HabitacionSerializer(habitaciones,many=True)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def create_habitacion(self,request):
        try:
            nueva_habitacion=HabitacionSerializer(data=request.data)
            if nueva_habitacion.is_valid():
                nueva_habitacion.save()
                return Response(nueva_habitacion.data,status=status.HTTP_201_CREATED)
        except:
            return Response(nueva_habitacion.errors,status=status.HTTP_400_BAD_REQUEST)
class HabitacionDetail(APIView):
    def get_object(self,pk):
        try:
            return Habitacion.object.get(pk=pk)
        except Habitacion.DoesNotExist:
            status.HTTP_404_NOT_FOUND

#Reserva
class ReservaList(APIView):
    pass
class ReservaDetail(APIView):
    pass

#Blog
class BlogList(APIView):
    pass
class BlogDetail(APIView):
    pass

