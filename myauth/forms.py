# forms for topic and posts


from django import forms
from .models import SignUpRequest, min_validator

from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
	demand = forms.CharField(widget=forms.Textarea, max_length=1000,min_validator=min_validator)
	class Meta:
		model = UserCreationForm
		fields = ['username','email','password1','password2'] 