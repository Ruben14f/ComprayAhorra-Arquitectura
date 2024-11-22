from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import Registro
from django.views.generic import CreateView
from django import forms

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            # Redirige al login después de registrarse
            return redirect(reverse('login') + '?register')
    else:
        form = Registro()

    # Personalización de los campos del formulario
    form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'tu_correo@gmail.com'})
    form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': '***********'})
    form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': '***********'})

    return render(request, 'register/register.html', {'form': form})