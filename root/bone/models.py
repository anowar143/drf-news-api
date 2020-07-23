from django.db import models

from user.models import User



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    created_by = models.ForeignKey(User, related_name='created_by_user', on_delete=models.CASCADE, )
    updated_by = models.ForeignKey(User, related_name='updated_by_user', on_delete=models.CASCADE)

    class Meta:
        abstract = True

