from django.contrib import admin
from django import forms
from . import models

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite


class PostInline(admin.TabularInline):
    """Adding extra object entry with empty box for directly entering new object"""
    model = models.Post
    fields = ("title", "body")
    extra = 1


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # Allow users to create object inline using PostInline
    inlines = [PostInline]
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class PostAdminForm(forms.ModelForm):
    """Overwrite default admin form with customized one"""
    class Meta:
        labels = {
            "title": "Blog Title",
            "name": "Name",
        }
    def clean(self):
        """Validation of form input for blog post body"""
        body = self.cleaned_data.get("body")
        if "<" in body:  # this just assumes that < is html tag...
            raise forms.ValidationError("Cannot use HTML tag")
        

class PostTitleFilter(admin.SimpleListFilter):
    """Create custom text filters"""
    title = "body"  # name of filter option displayed
    parameter_name = "body_contains"  # url parameter to be added

    def queryset(self, request, queryset):
        if self.value() is not None:  # self.value() is the value user entered for filtering
            return queryset.filter(body__icontains=self.value())  # body_icontains: if body contains value
        return queryset

    def lookups(self, request, model_admin):
        # left value is a search value, right value is what's displayed to user
        return [
            ("Blog", "Contains 'Blog'"),
            ("Dairy", "Contains 'Dairy'"),
            ("Develop", "Contains 'Develop'"),
        ]

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    # Fields for creating objects
    readonly_fields = ("created", "updated")
    fieldsets = [
        (None, {"fields": ("title", )}),
        ("contents", {"fields": ("body", )}),
        ("category", {"fields": ("category", "tag")}),
        ("meta", {"fields": ("published", "created", "updated")}),
    ]
    form = PostAdminForm
    filter_horizontal = ("tag", )  # filter UI for tag editing

    def save_model(self, request, obj, form, change):
        """add actions when post is saved on admin page"""
        print("before save")
        super().save_model(request, obj, form, change)
        print("after save")
    
    class Media:
        js = ("post.js", )  # load js file

    # Lists
    list_display = ('id', 'title', 'category', 'tags_summary', 'published', 'created', 'updated')  # tags are in a array
    list_select_related = ('category', )  # category is a fforeignkey which will cause many db access (n+1 problem). To avoid it, use list_select_related (must add , in it)
    list_editable = ('title', 'category')  # make fields editable
    search_fields = ('id', 'title', 'category__name', 'tag__name', 'created', 'updated')  # activate django default search feature. if object has properties, specify which one to search by adding '__property_name'
    ordering = ('-updated', '-created')  # sort results - indicates descending order
    list_filter = (PostTitleFilter, 'tag__name', 'created', 'updated')  # add filter options on the right handside
    actions = ("publish", "unpublish")

    def tags_summary(self, obj):
        """Concatenate all tags into single str"""
        qs = obj.tag.all()
        label = ', '.join(map(str, qs))
        return label

    tags_summary.short_description = 'tags'  # renaming column name from tags_summary to tags

    def get_queryset(self, request):
        """For many to many fields, avoid n+1 problem of accessing DB excessively"""
        # get list of posts
        qs = super().get_queryset(request)
        # pre-request tags data
        return qs.prefetch_related('tag')

    def publish(self, request, queryset):
        """Make queryset published"""
        # queryset is a set of objects user has selected with checkbox
        queryset.update(published=True)
    
    publish.short_description = "Publish"

    def unpublish(self, request, queryset):
        queryset.update(published=False)

    unpublish.short_description = "Unpublish"

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
