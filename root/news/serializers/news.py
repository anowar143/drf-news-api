from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    comments = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'img', 'article', 'created_at', 'updated_at', 'created_by', 'updated_by', 'comments')

