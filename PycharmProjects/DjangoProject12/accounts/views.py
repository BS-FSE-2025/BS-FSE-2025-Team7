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

            return redirect('setezin_map')  # Redirect back to the map page
    else:
        form = ReportForm()

    return render(request, 'report_problem.html', {'form': form})
def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import RegisterForm, RegisterForm2  # Ensure you import the forms correctly
from .models import Register, Register2, Login_1, Login_2  # Import models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register  # Assuming Register is your custom model for user registration

def login_(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user is registered by querying the Register model
        try:
            user_registration = Register.objects.get(username=username)
        except Register.DoesNotExist:
            messages.error(request, "You are not registered. Please sign up first.")
            return redirect('register')  # Redirect to the registration page

        # Authenticate the user using Django's built-in authentication system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in using Django's login system
            login(request, user)

            # Save login data to your custom Login_1 model (or similar)
            login_instance = Login_1(user=user, username=username, password=password)
            login_instance.save()  # Save the record

            messages.success(request, 'Logged in successfully!')
            return redirect('setezin_map')  # Redirect to the report issue page (or home)
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')  # Redirect to the login page

    return render(request, 'login.html')

def setezin_map(request):
    reports = Report.objects.all()  # Get all reports
    return render(request, 'setezin_map.html', {'reports': reports})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .forms import RegisterForm2
from .models import Register2, Login_2
from django.contrib.auth.models import User


from django.shortcuts import render
from .forms import RegisterForm, RegisterForm2, RegisterForm3
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm  # Assuming you're using RegisterForm
from .models import Register  # Assuming you're using Register model

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            birthday = form.cleaned_data['birthday']
            place = form.cleaned_data['place']

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists, please choose another.')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists, please choose another.')
                return redirect('register')

            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return redirect('register')

            try:
                # Create the User instance first
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                # Now create the Register instance, linking it to the user
                register_instance = form.save(commit=False)  # Prevent auto-save to modify
                register_instance.user = user  # Link to the created user
                register_instance.save()  # Save the Register instance

                messages.success(request, f'Account was created for {username}')
                return redirect('home')  # Redirect to the home page after successful registration

            except IntegrityError:
                messages.error(request, 'Username or email already exists.')
                return redirect('register')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# In your views.py (or wherever you are handling the form submission)

from django.contrib.auth.models import User
from .models import Register2

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import RegisterForm2  # Assuming Register2Form is your form for this registration
from .models import Register2  # Assuming Register2 is your model that stores additional info for this user type


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm2
from .models import Register2
from django.db import IntegrityError

def register2(request):
    if request.method == 'POST':
        form = RegisterForm2(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            work = form.cleaned_data['work']
            specialization = form.cleaned_data['specialization']

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists, please choose another.')
                return redirect('register2')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists, please choose another.')
                return redirect('register2')

            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return redirect('register2')

            try:
                # Create the User instance
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                # Create the Register2 instance to store additional information
                register_instance = Register2.objects.create(
                    user=user,
                    username=username,
                    email=email,
                    work=work,
                    specialization=specialization,
                    password1=password1,
                    password2=password2,
                )

                # Save the Register2 instance if needed
                register_instance.save()

                messages.success(request, f'Account was created for {username}')
                return redirect('home')  # Redirect to the home page after successful registration

            except IntegrityError:
                # Handle any database errors (like duplicate usernames/emails)
                messages.error(request, 'Username or email already exists.')
                return redirect('register2')  # Redirect back to the registration page

    else:
        form = RegisterForm2()

    return render(request, 'register2.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm3
from .models import Register3
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm3  # Import your RegisterForm3
from .models import Register3  # Import the Register3 model


def register3(request):
    if request.method == 'POST':
        form = RegisterForm3(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            phone_number = form.cleaned_data['phone']
            work = form.cleaned_data['work']
            department = form.cleaned_data['department']

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists, please choose another.')
                return redirect('register3')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists, please choose another.')
                return redirect('register3')

            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return redirect('register3')

            try:
                # Create the User instance first
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                # Now use the form to save the Register3 instance, linking it to the user
                register3_instance = form.save(commit=False)  # Prevent auto-save to modify
                register3_instance.user = user  # Link to the created user
                register3_instance.save()  # Save the Register3 instance

                messages.success(request, f'Account was created for {username}')
                return redirect('home')  # Redirect to the home page after successful registration

            except IntegrityError:
                messages.error(request, 'Username or email already exists.')
                return redirect('register3')

    else:
        form = RegisterForm3()

    return render(request, 'register3.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register2  # Assuming Register2 is your custom model for user registration (Engineering)

def login2(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user is registered by querying the Register2 model
        try:
            user_registration = Register2.objects.get(username=username)
        except Register2.DoesNotExist:
            return redirect('register2')  # Redirect to the registration page for Engineering

        # Authenticate the user using Django's built-in authentication system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in using Django's login system
            login(request, user)

            # Save login data to your custom Login_2 model
            login_instance = Login_2(user=user, username=username, password=password)
            login_instance.save()  # Save the record

            messages.success(request, 'Logged in successfully!')
            return redirect('reports_map')  # Redirect to the home page after successful login
        else:
            return redirect('login2')  # Redirect to the login page for Engineering

    return render(request, 'login2.html')

from django.shortcuts import render
from .models import Report

def reports_map(request):
    # Fetch all reports
    reports = Report.objects.all()
    return render(request, 'reports_map.html', {'reports': reports})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Report

@csrf_exempt  # Disable CSRF verification for simplicity, but secure it in production
def delete_report(request, report_id):
    if request.method == 'POST':
        try:
            report = Report.objects.get(id=report_id)
            report.delete()
            return JsonResponse({'status': 'success', 'message': 'Report deleted successfully.'})
        except Report.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Report not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
from django.shortcuts import render
from django.http import JsonResponse


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Report

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Report


from django.shortcuts import render
from .forms import RegisterForm3,Login3Form


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register3  # Assuming Register3 is your custom model for worker registration
from .forms import Login3Form

def login3(request):
    error_message = None
    if request.method == 'POST':
        form = Login3Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Check if the user is registered by querying the Register3 model
            try:
                user_registration = Register3.objects.get(username=username)
            except Register3.DoesNotExist:
                error_message = "You are not registered as a Worker. Please sign up first."
                return redirect('register3')  # Redirect to the registration page for Workers

            # Authenticate the user using Django's built-in authentication system
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page after login
                return redirect('home')  # Replace 'home' with your success URL
            else:
                error_message = "Invalid username or password."
    else:
        form = Login3Form()

    return render(request, 'login3.html', {'form': form, 'error_message': error_message})


from django.shortcuts import render
from django.http import JsonResponse
from .models import Message  # ודא ש-MESSAGE הוא המודל שלך
def chat_view(request):
    messages = Message.objects.order_by('timestamp')
    return render(request, 'chat_view.html', {'messages': messages})


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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Report
import json

import logging
logger = logging.getLogger(__name__)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Report

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Report

@csrf_exempt  # Exempt the view from CSRF verification (be cautious with this in production)
def update_status(request, report_id):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            status = data.get('status')

            # Validate the status
            if status not in dict(Report.STATUS_CHOICES):
                return JsonResponse({'error': 'Invalid status value'}, status=400)

            # Update the report status
            report = Report.objects.get(id=report_id)
            report.status = status
            report.save()

            return JsonResponse({'message': 'Status updated successfully'}, status=200)
        except Report.DoesNotExist:
            return JsonResponse({'error': 'Report not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            # Log the error (optional)
            print(f"Error updating status: {e}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
