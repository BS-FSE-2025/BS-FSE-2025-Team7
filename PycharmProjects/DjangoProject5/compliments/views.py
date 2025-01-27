from django.shortcuts import render, redirect
from .forms import ComplimentForm

def add_compliment(request):
    if request.method == 'POST':
        form = ComplimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to success page after saving the form
    else:
        form = ComplimentForm()

    return render(request, 'add_compliment.html', {'form': form})
