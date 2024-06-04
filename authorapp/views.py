from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Author
from .forms import AuthorForm


# Create your views here.

class AuthorListView(ListView):
    model = Author
    template_name = 'authorapp/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authorapp/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authorapp/author_form.html'
    success_url = reverse_lazy('author-list')

class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'authorapp/author_update.html'
    success_url = reverse_lazy('author-list')