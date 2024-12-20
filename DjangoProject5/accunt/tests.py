from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Rating

class RateComplaintTests(TestCase):

    def test_rate_complaint_form_submission_valid(self):
        # נוודא שבמידה והטופס תקין, המידע נשמר בבסיס הנתונים
        response = self.client.post(reverse('rate_complaint'), {
            'rating': 5,
            'comment': 'Excellent service!',
        })

        # נוודא שהנתונים נשמרו בבסיס הנתונים
        self.assertEqual(Rating.objects.count(), 1)
        rating = Rating.objects.first()
        self.assertEqual(rating.rating, 5)
        self.assertEqual(rating.comment, 'Excellent service!')

        # נוודא שהמשתמש מקבל הודעת הצלחה
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Thank you for your rating!')

        # נוודא שהמערכת מנווטת לדף ההצלחה
        self.assertRedirects(response, reverse('success'))

