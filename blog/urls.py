from . import views
from django.urls import path

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts/", views.AllPostView.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later"),
]

