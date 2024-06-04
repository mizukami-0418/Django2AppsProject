from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors/new/', views.AuthorCreateView.as_view(), name='author-create'),
    path('authors/update/<int:pk>/', views.AuthorUpdateView.as_view(), name='author-update'),
]
