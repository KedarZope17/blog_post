from django.urls import path
from . import views

#route over pages

urlpatterns = [
    path('', views.home, name="blog_home"),
    path('about/', views.about, name="blog_about")
]