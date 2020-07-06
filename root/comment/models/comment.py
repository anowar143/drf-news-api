from django.db import models

from news.models.news import News

from user.models import User


class Comment(models.Model):
    art = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', )
    write_a_comment = models.TextField(max_length=200, )
    usr = models.ForeignKey(User, related_name='comment_by_usr', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['art', 'write_a_comment']

    def __str__(self):
        return '%s %s' % (self.usr, self.write_a_comment)
