
from django.contrib.auth.models import User
from django.db import models
from django.db.models import IntegerField


# Create your models here.
class Grade(models.Model):
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField(default=0)

    def __str__(self):
        return self.grade