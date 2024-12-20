from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RatingForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RatingForm
from .models import Rating  # Import the Rating model


def rate_complaint(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            # עיבוד הדירוג והתגובה
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']

            # יצירת אובייקט Rating ושמירה בבסיס הנתונים
            Rating.objects.create(rating=rating, comment=comment)

            # הצגת הודעת הצלחה
            messages.success(request, "Thank you for your rating!")
            return redirect('success')  # עדכן לכתובת המתאימה
    else:
        form = RatingForm()

    return render(request, 'rate_complaint.html', {'form': form})


def success_page(request):
    return render(request, 'success.html', {})
from django.shortcuts import render

def rate_admin(request):
    return render(request, 'admin_page.html')  # Example page for /rate/admin/
