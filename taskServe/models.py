from django.contrib.auth.models import User
from django.db import models

CHAR_FIELD_MAX_LENGTH = 150


class Calendar(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH, unique=True)
    url = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    class TaskStatus(models.IntegerChoices):
        TO_DO = 1
        IN_PROGRESS = 2
        DONE = 3

    name = models.CharField(max_length=CHAR_FIELD_MAX_LENGTH)
    description = models.TextField()
    dueDate = models.DateTimeField()
    workDate = models.DateField()
    status = models.IntegerField(choices=TaskStatus.choices, default=TaskStatus.TO_DO)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, to_field='name')

    def __str__(self):
        return self.name
