from django import forms
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError

def add_placeholder(field, placeholder_value):
    field.widget.attrs['placeholder'] = placeholder_value

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add_placeholder(self.fields['email'], 'Ex.: exemplo@email.com')

    

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='*Senha'
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

        labels = {
            'username':'*Nome de usuário'
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Senhas precisam ser iguais',
                'password2': 'Senhas precisam ser iguais',
            })
            