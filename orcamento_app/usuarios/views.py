from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    orcamento = [
        {'item': 'Desenvolvimento Web', 'valor': 'R$ 2.500,00'},
        {'item': 'Hospedagem (12 meses)', 'valor': 'R$ 600,00'},
        {'item': 'Manutenção mensal (6 meses)', 'valor': 'R$ 900,00'},
    ]
    return render(request, 'dashboard.html', {'orcamento': orcamento})