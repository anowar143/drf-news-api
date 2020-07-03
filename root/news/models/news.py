from django.db import models

from bone.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=200, )
    article = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
