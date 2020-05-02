from django.urls import path

import blog

urlpatterns = [
    path("", blog.views.home, name="blog-home"),
    path("about/", blog.views.about, name="blog-about"),
]
