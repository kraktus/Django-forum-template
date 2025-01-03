# forms for topic and posts


from django import forms
from .models import SignUpRequest, min_validator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# More than registration, ask for a small text why they should be allowed
class UserCreationFormRequest(UserCreationForm):
    demand = forms.CharField(widget=forms.Textarea, max_length=1000,validators=min_validator)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'demand']