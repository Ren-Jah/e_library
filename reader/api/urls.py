from django.urls import include, path
from reader.api import viewset
from rest_framework.authtoken import views

urlpatterns = [
    path("signup", viewset.ReaderCreateView.as_view()),
    path("login", views.obtain_auth_token),
    path("list", viewset.ReaderListView.as_view()),
    path("<pk>", viewset.ReaderView.as_view()),
]