from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class PostListView(ListView):
    model = Post

    template_name = 'blog/post_list.html'
    # success_url = reverse_lazy('blog:all')


class PostCreateView(CreateView):
    model = Post

    template_name = 'blog/post_form.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    model = Post

    template_name = 'blog/post_detail.html'
    # success_url = reverse_lazy('blog:all')


class PostUpdateView(UpdateView):
    model = Post

    template_name = 'blog/post_form.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:all')

    # def get_success_url(self):


class PostDeleteView(DeleteView):
    model = Post

    template_name = 'blog/post_confirm_delete.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:all')
