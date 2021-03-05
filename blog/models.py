from django.db import models
from django.urls import reverse_lazy


class Blog(models.MOdel):
    title = models.CharFields(max_length=255)
    # url slug not to be duplicated
    slug = models.SlugField(unique=True)


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

    published = models.BooleanField(default=True)  # must be default=True if there is existing objects!

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # url is auto generated for a created page
        return reverse_lazy("create", args=[self.id])