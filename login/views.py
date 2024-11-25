from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def IniciarSesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Buscar el usuario por su email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            
            if user is not None:
                # Autenticación del usuario
                user = authenticate(request, username=user.username, password=password)
                
                if user is not None:
                    # Login del usuario
                    auth_login(request, user)
                    messages.success(request, "Has iniciado sesión correctamente.")
                    return redirect('inicio')  # Redirige a la página principal o al área de usuario
                else:
                    messages.error(request, "Credenciales incorrectas.")
            else:
                messages.error(request, "Usuario no encontrado.")
            return render(request, 'login/login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})
