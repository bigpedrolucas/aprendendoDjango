from django.urls import path
from .views import usuario

urlpatterns = [
    path('cadastro', usuario.cadastro, name='cadastro'),
    path('login', usuario.login, name='login'),
    path('dashboard', usuario.dashboard, name='dashboard'),
    path('logout', usuario.logout, name='logout'),
]
