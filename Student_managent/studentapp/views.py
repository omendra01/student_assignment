from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .token import get_token_for_user

#***************ADD CLASS VIEW***********************

class AddClassView(viewsets.ViewSet):
    serializer_class =AddClassSerializer
    def create(self,request):
        serializer =AddClassSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Records Create successfully.","data": serializer.data})
        return Response('error message')
    
    def list(self,request):
        queryset = AddClass.objects.all()
        serializer = AddClassSerializer(queryset,many=True)
        return Response({"message": "Records Retrieve successfully.","data": serializer.data})  

#***************STUDENT REGISTRATION VIEW**************

class studentRegistration(viewsets.ViewSet):
    serializer_class = StudentCreateUpdateSerializer

    def create(self,request):
        serializer = StudentCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Records Create successfully.","data": serializer.data}) 
        return Response('error message')
    
    def list(self,request):
        queryset = CustomUser.objects.all()
        serializer = StudentListSerializer(queryset,many=True)
        return Response({"message": "Records Retrieve successfully.","data": serializer.data}) 
    
    def retrieve(self,request,pk=None):
        try:
            queryset = CustomUser.objects.get(pk=pk)
            serializer = StudentListSerializer(instance=queryset)
            return Response({"message": "Records Retrieve successfully.","data": serializer.data}) 
        except:
            return Response('Record Not Found')
        
    def partial_update(self,request,pk=None):
        queryset = CustomUser.objects.get(pk=pk)
        serilaizer = StudentCreateUpdateSerializer(instance=queryset,data=request.data)
        if serilaizer.is_valid(raise_exception=True):
            serilaizer.save()
            return Response({"message": "Records Update successfully.","data": serilaizer.data})   
        return Response('Record Not Updated')

#*******************STUDENT SIGN IN VIEW******************

class StudentLoginView(viewsets.ViewSet):
    serializer_class = studentLoginSerializer
    def create(self,request):
        serializer = studentLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone = serializer.data.get('phone')
            password = serializer.data.get('password')
            user = authenticate(phone=phone,password=password)
            if user is not None and user.status=='active':
                token = get_token_for_user(user)
                return Response({'message':'logged in','token':token})
            return Response('Details Not Match')
        return Response("Error")    