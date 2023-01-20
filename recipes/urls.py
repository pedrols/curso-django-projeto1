
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    # criando url dinâmica (com id de inteiros)
    # importante ter um padrão para evitar brechas de segurança
    path('recipes/<int:id>/', views.recipe),
]
