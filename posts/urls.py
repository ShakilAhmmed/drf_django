from django.urls import path
from . import views
urlpatterns = [
    path('',views.posts,name="posts"),
    path('category',views.category,name="category"),
    path('post',views.post_html,name="post_html")
]