from django.db import models

# Create your models here.

# Auth request
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


min_validator=[
            MinLengthValidator(3, 'the field must contain at least 3 characters')
            ]

User = get_user_model()


class SignUpRequest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	accepted = models.BooleanField(default=False)
	demand = models.TextField(max_length=1000,validators=min_validator)

	def __str__(self):
		return f"{self.user}, {self.date}, {self.status}"