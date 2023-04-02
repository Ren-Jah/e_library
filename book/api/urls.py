from django.urls import include, path
from book.api import viewset

urlpatterns = [
    path("create", viewset.BookCreateView.as_view()),
    path("list", viewset.BookListView.as_view()),
    path("<pk>", viewset.BookView.as_view()),
]