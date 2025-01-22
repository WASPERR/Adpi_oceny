from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Grade(models.Model):
    grade = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.grade