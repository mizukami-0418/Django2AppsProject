from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/new/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>', views.BookUpdateView.as_view(), name='book-update'),
]
