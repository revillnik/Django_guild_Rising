from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("post/<slug:post_slug>/", views.ShowPost.as_view(), name="post"),
]
