from django.http import HttpResponse

from .models import Post, Category, Topic
from .forms import PostForm, TopicForm, CategoryForm

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


# @login_required
def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('index')
    else:
        form = CategoryForm()
        context = {
            "form": form,
        }
    return render(request, "forum/create_category.html", context)

def category(request, categ_slug, categ_id):
    category = get_object_or_404(Category, id=categ_id)
    topics = Topic.objects.filter(category=category)
    context = {
        "category":category,
        "topics":topics,
    }
    return render(request, "forum/category.html", context)

def topic(request, categ_slug, categ_id, topic_slug, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(topic=topic)
    context = {
        "topic":topic,
        "posts":posts,
    }
    return render(request, "forum/topic.html", context)


# @login_required
def new_topic(request, categ_slug, categ_id):
    category = get_object_or_404(Category, id=categ_id)
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.category = category
            topic.save()
            
            # Create first post
            post = Post.objects.create(
                user=request.user,
                content=request.POST.get('content'),
                topic=topic
            )
            return redirect('topic', categ_slug=categ_slug,categ_id=categ_id, topic_slug=topic.slug,topic_id=topic.id)
    else:
        form = TopicForm()
    
    context = {
        "form": form,
        "category": category,
    }
    return render(request, "forum/create_topic.html", context)



# @login_required
def create_post(request, categ_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.topic = topic
            post.save()
            return redirect('topic', categ_id=categ_id, topic_id=topic_id)
    else:
        form = PostForm()
    
    context = {
        "form": form,
        "topic": topic,
        "title": f"Reply to {topic.title}"
    }
    return render(request, "forum/create_post.html", context)


