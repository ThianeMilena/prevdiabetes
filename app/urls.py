from django.urls import path

from . import views

urlpatterns = [
    path('', views.receber_dados_paciente, name='receber_dados_paciente'),
]