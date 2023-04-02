from django.urls import include, path
from author.api import viewset

urlpatterns = [
    path("create", viewset.AuthorCreateView.as_view()),
    path("list", viewset.AuthorListView.as_view()),
    path("<pk>", viewset.AuthorView.as_view()),
]