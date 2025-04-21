from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    orcamentos = [
        {'id': 1, 'descricao': 'Orçamento A', 'valor': 1000},
        {'id': 2, 'descricao': 'Orçamento B', 'valor': 2000},
        {'id': 3, 'descricao': 'Orçamento C', 'valor': 3000},
    ]
    return render(request, 'index.html', {'orcamentos': orcamentos})