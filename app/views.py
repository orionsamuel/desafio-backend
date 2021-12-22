from django.core import paginator
from app.models import Alunos
from app.forms import AlunosForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    data = {}
    search = request.GET.get('search')
    all = Alunos.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    if search:
        data['db'] = Alunos.objects.filter(nome__icontains=search)
        paginator_src = Paginator(data['db'], 10)
        data['paginator'] = paginator_src.get_page(pages)
    else:
        data['paginator'] = paginator.get_page(pages)
    data['form'] = AlunosForm()
    return render(request, 'index.html', data)

def user_login(request):
    session = request.session.session_key
    if session:
        return redirect('/')
    else:
        return render(request, 'login.html')

def auth_user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        return user

@login_required(login_url='/login/')
def user_logout(request):
    if request.method == "GET":
        if request.GET.get('logout') == 'logout':
            logout(request)
            return redirect('/login/')
        else:
            return redirect('/')

@csrf_protect
def submit_login(request):
    logged_user = auth_user_login(request)

    if logged_user is not None:
        request.session['user_id'] = logged_user.id
        login(request, logged_user)
        
        return redirect('/')
    else:
        messages.error(request, "Usuário ou senha inválidos. Tente novamente!")
    return redirect('/login/')

@login_required(login_url='/login/')
def create(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

@login_required(login_url='/login/')
def update(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    form = AlunosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

@login_required(login_url='/login/')
def delete(request, pk):
    db = Alunos.objects.get(pk=pk)
    db.delete()
    return redirect('home')