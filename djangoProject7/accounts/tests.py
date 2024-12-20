from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Report


class ReportIssueTestCase(TestCase):

    def setUp(self):
        # Set up any pre-requisite data (if needed)
        self.url = reverse('report_issue')  # Adjust the URL name accordingly
        self.form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'description': 'Test description',
            'latitude': 40.7128,  # Normally, we will set these using the POST data
            'longitude': -74.0060,
        }

    def test_report_issue_form_valid(self):
        """Test the form submission with valid data"""
        # Simulating file upload (if applicable)
        photo = SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg')

        # Add the file to the form data (if there's an image field in the form)
        self.form_data['photo'] = photo

        # Simulate the form submission via POST request
        response = self.client.post(self.url, data=self.form_data)

        # Ensure the form is valid and is redirected after successful submission
        self.assertEqual(response.status_code, 302)  # 302 is the redirect status code
        self.assertRedirects(response, reverse('home'))  # Adjust to your success URL

        # Check that the form data was saved to the database
        report = Report.objects.last()  # Fetch the last saved report
        self.assertEqual(report.name, 'John Doe')
        self.assertEqual(report.email, 'john.doe@example.com')
        self.assertEqual(report.phone_number, '1234567890')
        self.assertEqual(report.description, 'Test description')
        self.assertEqual(report.latitude, 40.7128)
        self.assertEqual(report.longitude, -74.0060)
        self.assertIsNotNone(report.created_at)  # created_at should be set automatically

    def test_report_issue_form_invalid(self):
        """Test the form submission with invalid data (missing required fields)"""
        # Simulate a POST request with missing required fields (e.g., name)
        invalid_form_data = self.form_data.copy()
        invalid_form_data['name'] = ''  # Empty name to make the form invalid

        response = self.client.post(self.url, data=invalid_form_data)

        # Ensure the response contains the form with errors
        self.assertEqual(response.status_code, 200)  # The form should be re-rendered (status 200)
        self.assertFormError(response, 'form', 'name', 'This field is required.')  # Check specific form error

    def test_report_issue_file_upload(self):
        """Test file upload handling in the form"""
        photo = SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg')

        # Add the file to the form data
        self.form_data['photo'] = photo

        # Simulate the form submission via POST request with file
        response = self.client.post(self.url, data=self.form_data)

        # Check if the form was successfully submitted and redirected
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # Check if the file has been saved correctly (check the model)
        report = Report.objects.last()
        self.assertTrue(report.photo.name.startswith('photos/'))  # Ensure the photo is saved in the correct path

    def test_invalid_lat_long(self):
        """Test submitting invalid latitude and longitude values"""
        invalid_lat_long_data = self.form_data.copy()
        invalid_lat_long_data['location'] = 'invalid_latitude,invalid_longitude'  # Invalid format

        response = self.client.post(self.url, data=invalid_lat_long_data)

        # The form should still render because of invalid location data, but the rest should be valid
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'location',
                             'Invalid location data')  # Modify this if you have custom validation for location
