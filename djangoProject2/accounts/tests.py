from django.test import TestCase
from django.urls import reverse
from .models import Message
from django.http import JsonResponse


class SendMessageTests(TestCase):

    def test_send_message_success(self):
        """בדיקה לשליחת הודעה עם תוכן תקין"""
        data = {
            'username': 'User1',
            'content': 'Test message'
        }
        # שליחה של בקשה מסוג POST
        response = self.client.post(reverse('send_message'), data)

        # בדיקה שהסטטוס שהתקבל הוא success
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, 'utf8'), {'status': 'success'})

        # בדיקה שההודעה נשמרה במסד הנתונים
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.first().content, 'Test message')

    def test_send_message_no_content(self):
        """בדיקה לשליחת הודעה ללא תוכן"""
        data = {
            'username': 'User1',
            'content': ''
        }
        response = self.client.post(reverse('send_message'), data)

        # בדיקה שהסטטוס שהתקבל הוא error ושנרשם הודעת שגיאה
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, 'utf8'), {'status': 'error', 'message': 'No content provided'})

    def test_send_message_invalid_method(self):
        """בדיקה לשליחת בקשה לא-POST"""
        response = self.client.get(reverse('send_message'))  # GET במקום POST

        # בדיקה שהסטטוס שהתקבל הוא error (405)
        self.assertEqual(response.status_code, 405)
        self.assertJSONEqual(str(response.content, 'utf8'), {'status': 'error', 'message': 'Invalid request method'})
