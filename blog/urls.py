from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogHome, name="blogHome"),
    path("new/", views.addblog, name="addblog"),
    path("<int:pk>", views.blogDetails, name="blogDetails"),
    path("delete/<int:pk>/", views.deleteBlog, name="deleteBlog"),

]
