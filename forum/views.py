from django.http import HttpResponse

from .models import Post, Category, Topic
from .forms import PostForm, TopicForm

from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
# from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    categs = Category.objects.all()
    categs_with_topics = [(categ, Topic.objects.filter(category=categ).count()) for categ in categs]
    context = {
        "categs_with_topics":categs_with_topics,
    }
    print("categs_with_topics", categs_with_topics)
    return render(request, "forum/index.html", context)


def category(request, categ_id):
    category = get_object_or_404(Category, id=categ_id)
    topics = Topic.objects.filter(category=category)
    context = {
        "category":category,
        "topics":topics,
    }
    return render(request, "category.html", context)

def topic(request, _categ_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(topic=topic)
    context = {
        "topic":topic,
        "posts":posts,
    }
    return render(request, "topic.html", context)


@login_required
def new_topic(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "OZONE: Create New Post"
    })
    return render(request, "create_post.html", context)



@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "OZONE: Create New Post"
    })
    return render(request, "create_post.html", context)


