from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from asgiref.sync import sync_to_async
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader

from .models import Post, Category, Topic
from .forms import PostForm, TopicForm, CategoryForm

get_object_or_404_async = sync_to_async(get_object_or_404)

class IndexView(View):
    async def get(self, request):
        categs_with_topics = []
        async for categ in Category.objects.all():
            topic_count = await Topic.objects.filter(category=categ).acount()
            categs_with_topics.append((categ, topic_count))
        
        context = {
            "categs_with_topics": categs_with_topics,
        }
        return render(request, "forum/index.html", context)

class NewCategoryView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'forum.add_category'

    async def get(self, request):
        form = CategoryForm()
        context = {
            "form": form,
        }
        return render(request, "forum/create_category.html", context)

    async def post(self, request):
        form = CategoryForm(request.POST)
        if await sync_to_async(form.is_valid)():
            category = await sync_to_async(form.save)(commit=False)
            await category.asave()
            return redirect('index')
        context = {
            "form": form,
        }
        return render(request, "forum/create_category.html", context)

class CategoryView(View):
    async def get(self, request, categ_slug, categ_id):
        category = await get_object_or_404_async(Category, id=categ_id)
        topics = await Topic.objects.filter(category=category)
        context = {
            "category": category,
            "topics": topics,
        }
        return render(request, "forum/category.html", context)

class TopicView(View):
    async def get(self, request, categ_slug, categ_id, topic_slug, topic_id):
        topic = await get_object_or_404_async(Topic, id=topic_id)
        posts = await Post.objects.filter(topic=topic)
        form = PostForm()
        context = {
            "topic": topic,
            "posts": posts,
            "form": form,
        }
        return render(request, "forum/topic.html", context)

    async def post(self, request, categ_slug, categ_id, topic_slug, topic_id):
        topic = await get_object_or_404_async(Topic, id=topic_id)
        form = PostForm(request.POST)
        if await sync_to_async(form.is_valid)():
            post = await sync_to_async(form.save)(commit=False)
            post.user = request.user
            post.topic = topic
            await post.asave()
            return redirect('topic', categ_slug=categ_slug, categ_id=categ_id, 
                          topic_slug=topic_slug, topic_id=topic_id)
        posts = await Post.objects.filter(topic=topic)
        context = {
            "topic": topic,
            "posts": posts,
            "form": form,
        }
        return render(request, "forum/topic.html", context)

class NewTopicView(LoginRequiredMixin, View):
    async def get(self, request, categ_slug, categ_id):
        category = await get_object_or_404_async(Category, id=categ_id)
        form = TopicForm()
        context = {
            "form": form,
            "category": category,
        }
        return render(request, "forum/create_topic.html", context)

    async def post(self, request, categ_slug, categ_id):
        category = await get_object_or_404_async(Category, id=categ_id)
        form = TopicForm(request.POST)
        if await sync_to_async(form.is_valid)():
            topic = await sync_to_async(form.save)(commit=False)
            topic.user = request.user
            topic.category = category
            await topic.asave()
            
            # Create first post
            post = await Post.objects.create(
                user=request.user,
                content=request.POST.get('content'),
                topic=topic
            )
            return redirect('topic', categ_slug=categ_slug, categ_id=categ_id, 
                          topic_slug=topic.slug, topic_id=topic.id)
        
        context = {
            "form": form,
            "category": category,
        }
        return render(request, "forum/create_topic.html", context)

class CreatePostView(LoginRequiredMixin, View):
    async def get(self, request, categ_id, topic_id):
        topic = await get_object_or_404_async(Topic, id=topic_id)
        form = PostForm()
        context = {
            "form": form,
            "topic": topic,
            "title": f"Reply to {topic.title}"
        }
        return render(request, "forum/create_post.html", context)

    async def post(self, request, categ_id, topic_id):
        topic = await get_object_or_404_async(Topic, id=topic_id)
        form = PostForm(request.POST)
        if await sync_to_async(form.is_valid)():
            post = await sync_to_async(form.save)(commit=False)
            post.user = request.user
            post.topic = topic
            await post.asave()
            return redirect('topic', categ_id=categ_id, topic_id=topic_id)
        
        context = {
            "form": form,
            "topic": topic,
            "title": f"Reply to {topic.title}"
        }
        return render(request, "forum/create_post.html", context)


