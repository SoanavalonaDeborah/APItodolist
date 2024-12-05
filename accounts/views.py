from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
         # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            # Ajouter un message d'erreur si l'utilisateur existe
            messages.error(request, "This username was already taken.")
            return render(request, 'accounts/signup.html')
        else:
            # Créer un nouvel utilisateur si le nom n'est pas pris
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('tasks-list-create')
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('tasks-list-create')
        else:
            messages.error(request, 'Username or password incorrect.')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


