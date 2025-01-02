from django.db import models

# Create your models here.


# Auth request
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterRequest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	accepted = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.user}, {self.date}, {self.status}"