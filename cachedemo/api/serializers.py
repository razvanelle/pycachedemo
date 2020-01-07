from django.contrib.auth.models import User, Group
from rest_framework import serializers

from cachedemo.api import prjcache
from cachedemo.api.models import Project


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['id', 'name', 'created', 'updated', 'status']



