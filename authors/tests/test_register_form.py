from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized

class RegisterFormTess(TestCase):

    @parameterized.expand([
        ('username', '*Nome de usuário'),
        ('password', '*Senha'),
        ('password2', '*Confirme sua senha'),
    ])
    def test_label(self, field, label):
        form = RegisterForm()
        label2 = form[field].field.label
        self.assertEqual(label, label2)
        