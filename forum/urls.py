from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_category", views.new_category, name="new_category"),
    path("<categ_slug>/<int:categ_id>/", views.category, name="category"),
    path("<categ_slug>/<int:categ_id>/new", views.new_topic, name="new_topic"),
    path("<categ_slug>/<int:categ_id>/<topic_slug>/<int:topic_id>/", views.topic, name="topic"),
    path("<categ_slug>/<int:categ_id>/<topic_slug>/<int:topic_id>/", views.create_post, name="create_post"),
    # path("latest_posts", latest_posts, name="latest_posts"),
    # path("search", search_result, name="search_result"),
]
