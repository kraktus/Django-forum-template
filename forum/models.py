from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


min_validator=[
            MinLengthValidator(3, 'the field must contain at least 3 characters')
            ]

class Category(models.Model):
    title = models.CharField(max_length=50, validators=min_validator)
    slug = models.SlugField(max_length=400)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return f"{self.id},{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Topic(models.Model):
    title = models.CharField(max_length=400, validators=min_validator)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id},{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=100000,validators=min_validator)
    date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:100]

    