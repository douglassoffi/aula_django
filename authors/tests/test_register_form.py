from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized

class RegisterFormTess(TestCase):

    @parameterized.expand([
        ('username', '*Nome de usuário')
        ('password', '*Senha')
        ('password2', '*Confirme sua senha')
    ])
    def test_label(self, field, placeholder):
        form = RegisterForm()
        placeholder2 = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, placeholder2)
