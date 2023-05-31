from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("about/", views.about_category),
    path("main/", views.about_category),
    path("man/", views.man_category),
    path("small_kids/", views.small_kids_category),
    path("women/", views.women_category)
]
