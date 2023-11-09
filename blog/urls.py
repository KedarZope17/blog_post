from django.urls import path
from . import views

#route over pages

urlpatterns = [
    path('', views.landing_page, name="blog_landing_page"),
    path('home/', views.home, name="blog_home"),
    path('about/', views.about, name="blog_about")
]