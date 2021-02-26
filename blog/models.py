from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        unique=True,
    )

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        unique=True,
    )

    def __str__(self):
        return self.name

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )
    updated = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=True,
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
    )
    body = models.TextField(
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # url is auto generated for a created page
        return reverse_lazy("create", args=[self.id])