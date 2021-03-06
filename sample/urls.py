
from django.contrib import admin
from django.urls import path, include

from .views import Index, CSVView, PDFView, PeopleAPIView


urlpatterns = [
    path('', Index.as_view(), name="sample"),
    path('csv/', CSVView.as_view(), name="csv"),
    path('pdf/', PDFView.as_view(), name="pdf"),
    path('api/people/', PeopleAPIView.as_view(), name="people"),
]