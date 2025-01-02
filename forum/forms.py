# forms for topic and posts


from django import forms
from .models import Post, Topic, Category


# class Topic(models.Model):
#     title = models.CharField(max_length=400)
#     slug = models.SlugField(max_length=400, unique=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["content"]
	# min length for content and title

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ["title", "description"]

class TopicForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))
	class Meta:
		model = Topic
		fields = ["title"]