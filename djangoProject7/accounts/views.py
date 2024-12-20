from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm

def report_issue(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            # Get the location (latitude, longitude) from the form
            location = request.POST.get('location')
            if location:
                latitude, longitude = map(float, location.split(','))
                form.instance.latitude = latitude
                form.instance.longitude = longitude

            # Save the form data (including the file)
            form.save()

            return redirect('home')  # Adjust to your success page
    else:
        form = ReportForm()

    return render(request, 'report_problem.html', {'form': form})
def home(request):
    return render(request, 'home.html')
