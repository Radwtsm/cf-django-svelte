from django.urls import path
from . import views

urlpatterns = [

    path('persone/', views.getPersone, name='persone'),
    path('persone/<str:pk>/', views.getPersona, name='persona'),

]
