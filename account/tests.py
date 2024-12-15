from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from account.models import Login_1
from django.contrib.messages import get_messages
from account.models import Register2
from account.models import Login_2

class RegisterViewTest(TestCase):

    def setUp(self):
        # הגדרת נתונים נכונים להרשמה
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        # הגדרת נתונים לא נכונים (סיסמאות שאינן תואמות)
        self.invalid_data_password_mismatch = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'password123',
            'password2': 'password122'
        }

    def test_register_user_successful(self):
        response = self.client.post(reverse('register'), self.valid_data)
        self.assertEqual(response.status_code, 200)  # אם לא מבוצעת הפניה, ייתכן שתקבל תשובת 200

    def test_register_user_password_mismatch(self):
        response = self.client.post(reverse('register'), self.invalid_data_password_mismatch)
        self.assertEqual(response.status_code, 200)

class LoginViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.login_url = reverse('login')

    def test_login_successful(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'password123'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

        login_instance = Login_1.objects.filter(user=user).first()
        self.assertIsNotNone(login_instance)
        self.assertEqual(login_instance.username, 'testuser')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'loged in successful!')

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Invalid username or password')

        self.assertFalse('_auth_user_id' in self.client.session)

class Register2ViewTest(TestCase):

    def setUp(self):
        # הגדרת נתונים נכונים להרשמה
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        # הגדרת נתונים לא נכונים (סיסמאות שאינן תואמות)
        self.invalid_data_password_mismatch = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'password123',
            'password2': 'password122'
        }

    def test_register2_user_successful(self):
        response = self.client.post(reverse('register2'), self.valid_data)
        self.assertEqual(response.status_code, 200)  # אם לא מבוצעת הפניה, ייתכן שתקבל תשובת 200

    def test_register2_user_password_mismatch(self):
        response = self.client.post(reverse('register2'), self.invalid_data_password_mismatch)
        self.assertEqual(response.status_code, 200)


class Login2ViewTest(TestCase):

    def setUp(self):
        # Create a user to use for login
        self.user = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            password='password123'
        )

        # Valid login data
        self.valid_data = {
            'username': 'testuser2',
            'password': 'password123'
        }

        # Invalid login data (wrong password)
        self.invalid_data = {
            'username': 'testuser2',
            'password': 'wrongpassword'
        }

    def test_login_user_successful(self):
        response = self.client.post(reverse('login2'), self.valid_data)

        # Check if login was successful and redirected to home
        self.assertEqual(response.status_code, 302)  # Should redirect to home page
        self.assertRedirects(response, reverse('home'))

        # Check if the login data was saved
        login_instance = Login_2.objects.get(username='testuser2')
        self.assertEqual(login_instance.user.username, 'testuser2')

        # Check if success message is present
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Logged in successfully!')

    def test_login_user_invalid_credentials(self):
        response = self.client.post(reverse('login2'), self.invalid_data)



        # Check if error message is shown
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Invalid username or password')