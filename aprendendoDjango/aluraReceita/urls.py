
from django.contrib import admin
from django.urls import include, path

from receitas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('receitas.urls'))
]


