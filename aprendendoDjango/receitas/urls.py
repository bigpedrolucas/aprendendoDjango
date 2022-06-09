from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]