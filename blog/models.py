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
        verbose_name="Date created",  # overwrite default name displayed next to input box
    )
    updated = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=True,
        verbose_name="Date updated",
    )
    title = models.CharField(
        max_length=255,
        blank=False,
        null=True,
        verbose_name="Title",
    )
    body = models.TextField(
        blank=True,
        null=True,
        verbose_name="Body",
        help_text="HTML tags cannot be used.",  # show text just below form box
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Category",
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Tag",
    )

    published = models.BooleanField(
        default=True,
        verbose_name="Published",
    )  # must be default=True if there is existing objects!

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # url is auto generated for a created page
        return reverse_lazy("create", args=[self.id])