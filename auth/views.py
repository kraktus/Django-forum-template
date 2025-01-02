import asyncio
from django.http import HttpResponse
from django.views import View
# Create your views here.
from .models import RegisterRequest

    # path("register", views.register, name="register"),
    # path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout"),

 # class view
class RegisterView(View):
	def get(self, request):
		return HttpResponse("Register page")
	def post(self, request):
		return HttpResponse("Register page")

class LoginView(View):
	def get(self, request):
		return HttpResponse("Login page")
	def post(self, request):
		return HttpResponse("Login page")


def logout(request):
	return HttpResponse("Logout page")