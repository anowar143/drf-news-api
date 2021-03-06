from django.db import models

from bone.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=200, )
    img = models.FileField(blank=True, null=True, )
    article = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = 'news'
        verbose_name_plural = 'news'
