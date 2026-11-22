from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            # Save user
            user = form.save()

            # Send welcome email
            send_mail(
                'Welcome',
                'Welcome to Movie Website',
                'admin@gmail.com',
                [form.cleaned_data['email']],
            )

            return redirect('login')

    return render(
        request,
        'users/register.html',
        {'form': form}
    )
