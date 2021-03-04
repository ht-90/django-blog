from django.urls import path
from .views import Index, Detail, Create, Update, Delete
from .admin import mypage_site

urlpatterns = [
    path('blog/', Index.as_view(), name="index"),  # index page for blog - name - page name
    path('blog/detail/<pk>/', Detail.as_view(), name="detail"),  # detail page with param - pk: primary key
    path('blog/create/', Create.as_view(), name="create"),
    path('blog/update/<pk>/', Update.as_view(), name="update"),  # <pk> is required so user can select which post to update
    path('blog/delete/<pk>/', Delete.as_view(), name="delete"),
    path('mypage/', mypage_site.urls),  # user's admin page to manage own blog objects - access via blog/mypage/
]
