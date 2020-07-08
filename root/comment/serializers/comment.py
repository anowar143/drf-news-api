from rest_framework import serializers
from comment.models.comment import Comment

#t

class CommentSerializer(serializers.ModelSerializer):
    usr = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'article', 'write_a_comment', 'usr')
