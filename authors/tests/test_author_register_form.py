from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.urls import reverse

class AuthorRegisterFormTest(TestCase):
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

    @parameterized.expand([
        ('username', '*Nome de usuário'),
        ('password', '*Senha'),
        ('password2', '*Confirme sua senha'),
    ])
    def test_fields_label(self, field, label):
        form = RegisterForm()
        label2 = form[field].field.label

        self.assertEqual(label, label2)

    def test_username_min_length(self):
        self.form_data['username'] = 'a' * 3
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Este campo deve possuir no mínimo 4 caracteres.'

        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_username_max_length(self):
        self.form_data['username'] = 'a' * 51
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Este campo deve possuir no máximo 50 caracteres.'

        self.assertIn(msg, response.context['form'].errors.get('username'))
        
    def test_password_validation(self):
        self.form_data['password'] = 'senhafraca'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Senha deve possuir, ao menos, 1 letra maiúscula, 1 letra minúscula, 1 número e deve possuir no mínimo 8 caracteres.'

        self.assertIn(msg, response.context['form'].errors.get('password'))

    def test_password_and_password2_are_equal(self):
        self.form_data['password'] = 'SenhaForte1'
        self.form_data['password2'] = 'SenhaForte2'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Senhas precisam ser iguais'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.context['form'].errors.get('password2'))

    def test_register_create_only_accept_POST(self):
        url = reverse('authors:create')
        response = self.client.get(url)

        self.assertEqual(404, response.status_code)

    def test_author_is_registered_if_all_field_are_correct(self):
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)

        self.assertEqual(200, response.status_code)

    def test_email_is_not_create_if_already_in_use(self):
        url = reverse('authors:create')
        self.client.post(url, data=self.form_data, follow=True)
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'O e-mail informado já está em uso.'

        self.assertIn(msg, response.context['form'].errors.get('email'))
