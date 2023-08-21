from rest_framework import serializers
from .models import CustomUser,AddClass

#***************ADD CLASS SERIALIZER*********************

class AddClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddClass
        fields = ('id','class_name')

#************REGISTRATION LIST SERIALIZER*****************

class StudentListSerializer(serializers.ModelSerializer):
    class_name =AddClassSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields= ('id', 'phone', 'email', 'first_name', 'last_name', 'date_of_birth', 'status', 'class_name', 'image',)

#**********************REGISTRATION CREATE AND UPDATE SERIALISER***************

class StudentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields= ('id', 'phone', 'email', 'first_name', 'last_name', 'password','date_of_birth', 'status', 'class_name', 'image',)


    def create(self, validated_data):
        password = validated_data.pop('password',None)
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

#********************LOGIN SERIALIZER******************
   
class studentLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)    