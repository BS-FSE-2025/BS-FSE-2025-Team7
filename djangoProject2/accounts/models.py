from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")  # שם משתמש
    content = models.TextField()  # תוכן ההודעה
    timestamp = models.DateTimeField(auto_now_add=True)  # זמן יצירת ההודעה

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"  # הצגה קצרה של ההודעה
