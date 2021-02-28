"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from registration.views import SignUpView, ActivateView

index_view =TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(index_view), name="registration"),
    path('', include("django.contrib.auth.urls")),
    path('website/', include('website.urls')),  # direct request to website.urls
    path('blog/', include('blog.urls')),  # direct request to blog.urls
    path('form/', include('form.urls')), 
    path('signup/', SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),  # receive user id and token for activate page
]
