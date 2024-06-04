from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'bookapp/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'bookapp/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'bookapp/book_update.html'
    success_url = reverse_lazy('book-list')