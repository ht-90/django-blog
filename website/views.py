from django.shortcuts import render
from django.views.generic import TemplateView


# Top page
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "NAME"
        return ctxt

# About page
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 3
        ctxt["skillset"] = [
            "Python",
            "JavaScript",
            "HTML / CSS",
            "PostgreSQL",
        ]
        return ctxt
