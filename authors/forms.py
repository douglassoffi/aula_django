from django import forms
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
import re

# def add_placeholder(field, placeholder_value):
#     field.widget.attrs['placeholder'] = placeholder_value

def password_validation(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Senha deve possuir, ao menos, 1 letra maiúscula, 1 letra minúscula, 1 número e deve possuir no mínimo 8 caracteres.'
        ),
            code='invalid'
        )

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # add_placeholder(self.fields['email'], 'Ex.: exemplo@email.com')

    username = forms.CharField(
        required=True,
        label='*Nome de usuário',
        min_length=4, max_length=50,
        error_messages={
            'min_length': 'Este campo deve possuir no mínimo 4 caracteres.',
            'max_length': 'Este campo deve possuir no máximo 50 caracteres.'
        }
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='*Senha',
        validators=[password_validation]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='*Confirme sua senha'
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'O e-mail informado já está em uso.',
                code='Invalid',
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Senhas precisam ser iguais',
                'password2': 'Senhas precisam ser iguais',
            },
            code='Invalid')
            