from django.urls import path, include
from form.views import Index

urlpatterns = [
    path('', Index.as_view(), name="form")
]
