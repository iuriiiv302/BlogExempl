from django.contrib.auth.models import User, Group
from .models import Blog
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class likeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('likes')

