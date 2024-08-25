from django.shortcuts import render, redirect
from django.views import View
from reminders.models import User

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # Extract the POST data
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username, password=password).exists():
            return redirect('homepage')

class Main(View):
    def get(self, request):
        return render(request, 'mainpage.html')