from rest_framework import serializers

from .models import Task, Calendar


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'dueDate', 'workDate', 'status', 'owner', 'calendar']


class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'name', 'url', 'owner']
