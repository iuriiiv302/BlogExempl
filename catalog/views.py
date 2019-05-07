from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from catalog.serializers import UserSerializer, GroupSerializer
from .models import Blog
from django.contrib.auth.models import User, Group



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def allblogs(request):
    blogs = Blog.objects
    return render(request, 'catalog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'catalog/details.html', {'blog': blogdetail})


def likes(requset):
    fields = Blog._meta.get_fields()
    my_field = Blog._meta.get_field('likes')
    return my_field



