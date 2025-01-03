from django.db import models
from django.conf import settings
# Create your models here.

# Auth request
from django.core.validators import MinLengthValidator


min_validator=[
            MinLengthValidator(3, 'the field must contain at least 3 characters')
            ]


class SignUpRequest(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	demand = models.TextField(max_length=1000,validators=min_validator)

	def __str__(self):
		return f"{self.user}, {self.date}, {self.status}"