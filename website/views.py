from django.shortcuts import render
from django.views.generic import TemplateView


# Top page
class IndexView(TemplateView):
    template_name = "index.html"


# About page
class AboutView(TemplateView):
    template_name = "about.html"