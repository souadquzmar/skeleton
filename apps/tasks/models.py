from django.db import models
from apps.users.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
