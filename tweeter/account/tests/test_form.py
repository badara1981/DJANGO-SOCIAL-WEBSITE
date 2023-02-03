from account.forms import LoginForm, UserRegistrationForm
from django.test import SimpleTestCase, TransactionTestCase


class TestForm(SimpleTestCase):
    def test_form_with_valid_data(self):
        form = LoginForm(data={
            'username': 'username',
            'password': 'pass'
        })

        self.assertTrue(form.is_valid())

    def test_form_with_uncorect_data(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


class TestRegisterForm(TransactionTestCase):
    def test_form_with_valid_data(self):
        form = UserRegistrationForm(data={
            'username': 'username',
            'first_name': 'badara',
            'email': 'badara.jammeh@hotmail.com',
            'password': 'bakau1981',
            'password2': 'bakau1981'
        })
        self.assertTrue(form.is_valid())