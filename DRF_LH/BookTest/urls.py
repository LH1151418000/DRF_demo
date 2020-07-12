from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooksAPIView.as_view()),
    path('books/<pk>/', views.BookAPIView.as_view()),
]
