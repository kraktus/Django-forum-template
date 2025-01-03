from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("new_category", views.NewCategoryView.as_view(), name="new_category"),
    path("<categ_slug>/<int:categ_id>/", views.CategoryView.as_view(), name="category"),
    path("<categ_slug>/<int:categ_id>/new", views.NewTopicView.as_view(), name="new_topic"),
    path("<categ_slug>/<int:categ_id>/<topic_slug>/<int:topic_id>/", views.TopicView.as_view(), name="topic"),
    path("<categ_slug>/<int:categ_id>/<topic_slug>/<int:topic_id>/post", views.CreatePostView.as_view(), name="create_post"),
]
