from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse

class RegisterFormTest(TestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'first_name': 'first',
            'last_name': 'last',
            'username': 'user',
            'email': 'email@email.com',
            'password': 'Password123',
            'password2': 'Password123',
        }
        return super().setUp(*args, **kwargs)
 
    @parameterized.expand([
        ('username', 'Este campo é obrigatório.'),
        ('password', 'Este campo é obrigatório.'),
        ('password2', 'Este campo é obrigatório.'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.context['form'].errors.get(field))
