from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Receita

def home(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicado=True)

    dados = {
        'receitas': receitas
    }
    return render(request, 'home.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)
