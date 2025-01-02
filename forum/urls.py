from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:categ_id>/", views.category, name="category"),
    path("category/<int:categ_id>/new/", views.new_topic, name="new_topic"),
    path("category/<int:categ_id>/topic/<int:topic_id>/", views.topic, name="topic"),
    path("category/<int:categ_id>/topic/<int:topic_id>/reply/", views.create_post, name="create_post"),
    # path("latest_posts", latest_posts, name="latest_posts"),
    # path("search", search_result, name="search_result"),
]
