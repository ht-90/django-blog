from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post


# List of models
class Index(ListView):
    # Define models to list on a page
    model = Post


# List of models in detail
class Detail(DetailView):
    # Define models to list for details
    model = Post


# Create a post
class Create(CreateView):
    model = Post

    # Fields to let users to edit
    fields = ["title", "body", "category", "tag"]


# Update a post
class Update(UpdateView):
    model = Post

    # Fields to let users to edit
    fields = ["title", "body", "category", "tag"]


class Delete(DeleteView):
    model = Post

    # Redirect page on delete
    success_url = "/"
