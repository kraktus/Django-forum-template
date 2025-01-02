from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<categ_slug>/<int:categ_id>", views.category, name="categ"),
    path("<categ_slug>/<int:categ_id>/<topic_slug>/<int:topic_id>", views.topic, name="topic"),
    # path("create_post", create_post, name="create_post"),
    # path("latest_posts", latest_posts, name="latest_posts"),
    # path("search", search_result, name="search_result"),
]