from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.postgres.search import SearchVector
from rest_framework.pagination import PageNumberPagination

# Create your views here.
@api_view(['GET'])
def list_users(request):
    users = Users.objects.all().order_by('first_name')
    if request.query_params.get('search'):
        search = request.query_params.get('search')
        type = request.query_params.get('type')
        if type == "all":
            users = Users.objects.annotate(
                search=SearchVector('first_name', 'last_name', 'email'),
            ).filter(search=search)
        elif type == "first_name":
            users = Users.objects.annotate(
                search=SearchVector('first_name'),
            ).filter(search=search)
        elif type == 'last_name':
            users = Users.objects.annotate(
                search=SearchVector('last_name'),
            ).filter(search=search)
        elif type == 'email':
            users = Users.objects.annotate(
                search=SearchVector('email'),
            ).filter(search=search)

    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(users, request)
    serializer = UsersSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

def lookup_users(request):
    return render(request, 'users.html')