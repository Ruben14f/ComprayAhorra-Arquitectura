from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        help_text="Requerido, 254 caracteres como máximo y debe ser válido", 
        error_messages={'invalid': 'Introduce una dirección de correo electrónico válida.'},
        label="Correo electronico"
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado. Prueba con otro.")
        return email



class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'placeholder': 'tu@gmail.com'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': '********'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():  # Verifica si el email está registrado
            raise ValidationError("Este correo electrónico no está registrado.")
        return email
