from django.db import models

from django.contrib.auth.models import User

import datetime

class Rooms(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name


class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    room_name = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='problems')
    solve = models.BooleanField(default=False)
    date_publish = models.DateTimeField(default=datetime.datetime.now())
    date_solve = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.message[:10]

