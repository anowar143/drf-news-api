from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.CASCADE, default='User', )
    updated_by = models.ForeignKey(User, related_name='updated_by_user', on_delete=models.CASCADE, default='User')

    class Meta:
        abstract = True
