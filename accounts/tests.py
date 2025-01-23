from django.test import TestCase

# Create your tests here.
class HomeViewTests(TestCase):

    def setUp(self):
        """Set up the necessary test data."""
        self.url = reverse('home')  # Adjust to your actual URL name for the home view

    def test_home_get_request(self):
        """Test the GET request for the home view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')  # Replace with the correct template name


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Register, Login_1

class LoginViewTests(TestCase):

    def setUp(self):
        """Set up necessary test data."""
        self.url = reverse('login')  # Adjust to your actual URL name for login
        self.username = 'testuser'
        self.password = 'testpassword'
        # Create a user for testing login
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_page_get_request(self):
        """Test the GET request for the login view."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')  # Adjust to your actual template name

    def test_login_post_unregistered_user(self):
        """Test the POST request for login with an unregistered user."""
        # Use a username that is not in the Register model (i.e., not registered)
        response = self.client.post(self.url, {'username': 'unregistered_user', 'password': 'somepassword'})

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertRedirects(response, '/register/')  # Should redirect to registration page


from django.test import TestCase
from django.urls import reverse
from .models import Report


class Register2ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register2')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'work': 'Software Engineer',
            'specialization': 'Web Development',
        }
        self.invalid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'mismatchedpassword',  # Passwords do not match
            'work': 'Software Engineer',
            'specialization': 'Web Development',
        }

    def test_register_valid_data(self):
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)  # Redirects after successful registration


    def test_register_username_already_exists(self):
      User.objects.create_user(username='testuser', email='existing@example.com', password='securepassword123')
      response = self.client.post(self.register_url, self.valid_data)
      self.assertEqual(response.status_code, 200)  # Redirects back to registration page

    def test_register_get_request(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_email_already_exists(self):
        User.objects.create_user(username='otheruser', email='testuser@example.com', password='securepassword123')
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)  # Redirects back to registration page

class Register3ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register3')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'phone': '1234567890',
            'work': 'Software Engineer',
            'department': 'Development',
        }
        self.invalid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword123',
            'password2': 'mismatchedpassword',  # Passwords do not match
            'phone': '1234567890',
            'work': 'Software Engineer',
            'department': 'Development',
        }

    def test_register_valid_data(self):
        response = self.client.post(self.register_url, self.valid_data)
        self.assertEqual(response.status_code, 200)  # Redirects after successful registration

    def test_register_get_request(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register3.html')

    def test_register_passwords_do_not_match(self):
        response = self.client.post(self.register_url, self.invalid_data)
        self.assertEqual(response.status_code, 200)  # Redirects back to registration page
        self.assertContains(response, 'Passwords do not match.', html=True)

        class Login2ViewTest(TestCase):
            def setUp(self):
                self.client = Client()
                self.login_url = reverse('login2')
                self.register_url = reverse('register2')
                self.reports_map_url = reverse('reports_map')

                # Create a test user and corresponding Register2 entry
                self.user = User.objects.create_user(username='testuser', password='securepassword123')
                self.registered_user = Register2.objects.create(
                    user=self.user,
                    username='testuser',
                    email='testuser@example.com',
                    work='Software Engineer',
                    specialization='Web Development',
                    password1='securepassword123',
                    password2='securepassword123',
                )

            def test_login_valid_credentials(self):
                response = self.client.post(self.login_url, {
                    'username': 'testuser',
                    'password': 'securepassword123',
                })
                self.assertEqual(response.status_code, 302)  # Redirects after successful login
                self.assertRedirects(response, self.reports_map_url)
                self.assertTrue(Login_2.objects.filter(username='testuser').exists())

            def test_login_invalid_username(self):
                response = self.client.post(self.login_url, {
                    'username': 'invaliduser',
                    'password': 'securepassword123',
                })
                self.assertEqual(response.status_code, 302)  # Redirects to register2 page
                self.assertRedirects(response, self.register_url)

        class Login3ViewTest(TestCase):

            def setUp(self):
                # Create a Django User for authentication
                self.user = User.objects.create_user(username='worker', password='password')

            def test_login3_success(self):
                # Send a POST request with correct username and password
                response = self.client.post(reverse('login3'), {'username': 'worker', 'password': 'password'})

            def test_login3_get_request(self):
                # Send a GET request to the login view
                response = self.client.get(reverse('login3'))

                # Ensure the form is present in the response
                self.assertContains(response, '<form')
                self.assertEqual(response.status_code, 200)

            def test_login3_invalid_credentials(self):
                # Send a POST request with incorrect password
                response = self.client.post(reverse('login3'), {'username': 'worker', 'password': 'wrongpassword'})
                self.assertEqual(response.status_code, 302)


