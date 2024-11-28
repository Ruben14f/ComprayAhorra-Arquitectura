from django.shortcuts import redirect, render
from django.urls import reverse
from core.forms import RegisterForm
from django import forms

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario
            # Redirige al login después de registrarse
            return redirect(reverse('login') + '?register')
    else:
        form = RegisterForm()

    # Personalización de los campos del formulario
    form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'tu_correo@gmail.com'})
    form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': '***********'})
    form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': '***********'})

    return render(request, 'core/register/register.html', {'form': form})