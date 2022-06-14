from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def cadastro(request):
    """Cadastra um usuário"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 
        if campo_vazio(nome): ##Se o campo nome está vazio
            messages.error(request, 'O campo nome não pode estar vazio!')
            return redirect('cadastro')
        if campo_vazio(email): ##Se o campo email está vazio
            messages.error(request, 'O campo email não pode estar vazio!')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(password, password2): ##Se as senhas 1 e 2 são diferentes
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists(): ##Se o email já está cadastrado
            messages.error(request, 'Email já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists(): ##Se o email já está cadastrado
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('cadastro')      
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """Autentica o login do usuário"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        ##print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Email ou senha não conferem. Verifique os campos e tente novamente')
                return render(request, 'usuarios/login.html')
        else:
            messages.error(request, 'Usuário não encontrado')
            return render(request, 'usuarios/login.html')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def dashboard(request):
    """Painel do usuário logado"""
    if request.user.is_authenticated:
        id = request.user.id
        lista_receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)

        dados = {
            'receitas' : lista_receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('home')

def campo_vazio(campo):
    """Função reaproveitável para verificar se um campo de form está vazio"""
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    """Verifica se os campos de senha conferem"""
    return senha != senha2