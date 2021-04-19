from account.forms import LoginForm
from django.test import SimpleTestCase


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