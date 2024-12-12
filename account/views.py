from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import RegisterForm, RegisterForm2  # Ensure you import the forms correctly
from .models import Register, Register2, Login_1, Login_2  # Import models


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            phone_number = form.cleaned_data['phone_number']
            password2 = form.cleaned_data['password2']
            try:
                # Create a User instance
                user = User.objects.create_user(
                    username=username,  # Use the username as provided
                    email=email,
                    password=password1
                )

                # Create a Register instance (storing additional info)
                Register.objects.create(
                    user=user,
                    username=username,  # You might not need this if using User.username
                    email=email,
                    phone_number=phone_number,
                    password1=password1,
                    password2=password2,
                )

                messages.success(request, f'Account was created for {username}')
                return redirect('home')

            except IntegrityError:
                messages.error(request, 'Username or email already exists.')
                return redirect('register')  # Redirect back to the registration page
    else:

        form = RegisterForm()

    return render(request, 'register.html', {'form': form})




def login_(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user with Django's built-in system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in using Django's login system
            login(request, user)

            # Save login data to your custom Login_1 model
            login_instance = Login_1(user=user, username=username,
                                     password=password)  # Assign user to Login_1
            login_instance.save()  # Save the record
            messages.success(request,'loged in successful!')
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from .forms import RegisterForm2
from .models import Register2, Login_2
from django.contrib.auth.models import User


def register2(request):
    if request.method == 'POST':
        form = RegisterForm2(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            phone_number = form.cleaned_data['phone_number']
            password2 = form.cleaned_data['password2']

            try:
                # Create a User instance
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                # Create a Register2 instance (storing additional info)
                Register2.objects.create(
                    user=user,
                    username=username,
                    email=email,
                    phone_number=phone_number,
                    password1=password1,
                    password2=password2,
                )

                messages.success(request, f'Account was created for {username}')
                return redirect('home')

            except IntegrityError:
                messages.error(request, 'Username or email already exists.')
                return redirect('register2')  # Redirect back to the registration page
    else:
        form = RegisterForm2()

    return render(request, 'register2.html', {'form': form})


def login2(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user with Django's built-in system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in using Django's login system
            login(request, user)

            # Save login data to your custom Login_2 model
            login_instance = Login_2(user=user, username=username, password=password)
            login_instance.save()  # Save the record

            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login2')

    return render(request, 'login2.html')
