from django.contrib import admin
from .models import AddClass,CustomUser

@admin.register(AddClass)
class AddClassAdmin(admin.ModelAdmin):
    list_display=['id','class_name']

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display =['id','phone','email','first_name','last_name']