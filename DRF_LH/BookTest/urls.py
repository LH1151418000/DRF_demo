from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BooksView.as_view()),
    path('books/<pk>/', views.BookView.as_view()),
]
