import asyncio
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import SignUpRequest

from django.shortcuts import redirect, render, get_object_or_404

    # path("register", views.register, name="register"),
    # path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout"),

 # class view
class SignUpView(View):
    async def get(self, request):
        return render(request, "auth/signup.html")
    async def post(self, request):
        form = SignUpRequest(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('index')
        else:
            return HttpResponse("Error")