from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import HabitacionSerializer,ReservaSerializer,UserSerializer,UserLoginSerializer
from .models import Habitacion,Reserva
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
#User
class RegisterView(APIView):
    @swagger_auto_schema(
        operation_summary='Resgistrarse',
        request_body=UserSerializer,
        responses={201:UserSerializer()},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    @swagger_auto_schema(
        operation_summary='Iniciar Sesion',
        request_body=UserLoginSerializer,
        responses={201:UserLoginSerializer()},
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                # Usuario autenticado correctamente
                return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
            else:
                # Credenciales inválidas
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Habitacion
class HabitacionList(APIView):
    @swagger_auto_schema(
        operation_summary='Listar Habitaciones',
        responses={200:HabitacionSerializer(many=True)},
    )
    def get(self,request):
        habitaciones=Habitacion.objects.all()
        serializer=HabitacionSerializer(habitaciones,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(
        operation_summary='Crear Habitacion',
        request_body=HabitacionSerializer,
        responses={201:HabitacionSerializer()},
    )
    def post(self,request):
        nueva_habitacion=HabitacionSerializer(data=request.data)
        if nueva_habitacion.is_valid():
            nueva_habitacion.save()
            return Response(nueva_habitacion.data,status=status.HTTP_201_CREATED)
        return Response(nueva_habitacion.errors,status=status.HTTP_400_BAD_REQUEST)
        
class HabitacionDetail(APIView):
    def get_object(self,pk):
        try:
            return Habitacion.object.get(pk=pk)
        except Habitacion.DoesNotExist:
            status.HTTP_404_NOT_FOUND

    @swagger_auto_schema(
        operation_summary='Eliminar Habitacion',
        responses={204:HabitacionSerializer() },
    )
    def delete(self,pk):
        habitacion=self.get_object(pk)
        try :
            habitacion.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except: raise status.HTTP_204_NO_CONTENT
    
    @swagger_auto_schema(
        operation_summary='Buscar Habitacion',
        responses={200:HabitacionSerializer() } , 
    )
    def get_detail(self,pk):
        habitacion=self.get_object(pk)
        serializer=HabitacionSerializer(habitacion)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary='Actualizar Habitacion',
        request_body=HabitacionSerializer,
        responses={200:HabitacionSerializer() },
    )
    def put(self,request,pk):
        habitacion=self.get_object(pk)
        serializer=HabitacionSerializer(habitacion,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Reserva
class ReservaList(APIView):
    @swagger_auto_schema(
        operation_summary='Listar Reserva',
        responses={200:ReservaSerializer(many=True)}, 
    )
    def get(self):
        try:
           reservas=Reserva.objects.all()
           serializer=ReservaSerializer(reservas,many=True)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        operation_summary='Crear Reserva',
        request_body=ReservaSerializer,
        responses={201:ReservaSerializer()},  
    )
    def post(self,request):
        try:
            nueva_reserva=ReservaSerializer(data=request.data)
            if nueva_reserva.is_valid():
                nueva_reserva.save()
                return Response(nueva_reserva.data,status=status.HTTP_201_CREATED)
        except:
            return Response(nueva_reserva.errors,status=status.HTTP_400_BAD_REQUEST)
 
class ReservaDetail(APIView):
    def get_object(self,pk):
        try:
            return Reserva.object.get(pk=pk)
        except Reserva.DoesNotExist:
            status.HTTP_404_NOT_FOUND

    @swagger_auto_schema(
        operation_summary='Eliminar Reserva',
        responses={204:ReservaSerializer()},
    )
    def delete(self,pk):
        reserva=self.get_object(pk)
        try :
            reserva.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except: raise status.HTTP_204_NO_CONTENT
    
    @swagger_auto_schema(
        operation_summary='Buscar Reserva',
        responses={200:ReservaSerializer()},
    )
    def get_detail(self,pk):
        reserva=self.get_object(pk)
        serializer=ReservaSerializer(reserva)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_summary='Actualizar Reserva',
        request_body=ReservaSerializer,
        responses={200:ReservaSerializer()},
    )
    def put(self,request,pk):
        reserva=self.get_object(pk)
        serializer=ReservaSerializer(reserva,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Blog
class BlogList(APIView):
    pass
class BlogDetail(APIView):
    pass

