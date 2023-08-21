from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('registration',views.studentRegistration,basename='registration')
router.register('student-signin',views.StudentLoginView,basename='student-signin')
router.register('addclass',views.AddClassView,basename='addclass')

urlpatterns = [
    path('',include(router.urls)),
   
]