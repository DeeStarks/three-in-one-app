from .views import list_users, lookup_users
from django.urls import path

apps_name = 'search_app'

urlpatterns = [
    path("api/users/", list_users, name='api_list_users'),
    path("users/", lookup_users, name='lookup'),
]