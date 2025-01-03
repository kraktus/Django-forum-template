import asyncio
from django.http import HttpResponse
from django.views import View
from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UserCreationFormRequest
from django.contrib.auth import alogin

from django.shortcuts import redirect, render, get_object_or_404

 # class view
class SignUpView(View):
    async def get(self, request):
        form = UserCreationFormRequest()
        context = {
            "form": form,
        }
        return render(request, "myauth/signup.html", context)
    async def post(self, request):
        form = UserCreationFormRequest(request.POST)
        if await sync_to_async(form.is_valid)():
            user = await sync_to_async(form.save)(commit=False)
            user.username = user.username.lower()
            await user.asave()
            await alogin(request, user)
            return redirect('index')
        else:
            return render(request, "myauth/signup.html", {"form": form})