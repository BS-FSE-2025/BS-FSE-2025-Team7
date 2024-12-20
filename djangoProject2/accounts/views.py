from django.shortcuts import render
from django.http import JsonResponse
from .models import Message  # ודא ש-MESSAGE הוא המודל שלך


def chat_view(request):
    messages = Message.objects.order_by('timestamp')
    return render(request, 'chat/chat_view.html', {'messages': messages})


def send_message(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'Anonymous')  # אם לא נמסר שם משתמש, השתמש ב-"Anonymous"
        content = request.POST.get('content')

        if content:
            # אם יש תוכן להודעה, צור הודעה חדשה
            Message.objects.create(name=username, content=content)
            return JsonResponse({'status': 'success'})
        else:
            # אם אין תוכן בהודעה, החזר שגיאה
            return JsonResponse({'status': 'error', 'message': 'No content provided'}, status=400)

    # אם לא נשלחה בקשה מסוג POST
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
