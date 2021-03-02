from django.contrib import admin
from . import models

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass


# Admin page of user's
class BlogAdminSite(AdminSite):
    site_header = 'My Page'
    site_title = 'My Page'
    index_title = 'Home'
    # Hide site url link on navbar
    site_url = None

    # Allow user to access User Admin page
    login_form = AuthenticationForm
    def has_permission(self, request):
        return request.user.is_active

# Create an instance and add objects to admin page
mypage_site = BlogAdminSite(name="mypage")
mypage_site.register(models.Post)
mypage_site.register(models.Category)
mypage_site.register(models.Tag)
