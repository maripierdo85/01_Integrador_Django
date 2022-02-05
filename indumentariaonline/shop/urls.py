from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contacto', views.contacto,name='contacto'),
    path('index_2', views.index_2,name='index_2'),
    path('contacto_2', views.contacto_2,name='contacto_2')
]