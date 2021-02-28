from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from .forms import SignUpForm, activate_user


class SignUpView(CreateView):
    form_class = SignUpForm
    successful_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        # Check user token
        result = activate_user(uidb64, token)
        # Pass boolean result to context
        return super().get(request, result=result, **kwargs)
    