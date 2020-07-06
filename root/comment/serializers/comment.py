from rest_framework import serializers
from comment.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    usr = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Comment
        fields = ('art', 'write_a_comment', 'usr')
