from rest_framework import serializers
from news.models.news import News


class NewsSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    comments = serializers.StringRelatedField(read_only=True, many=True)


    class Meta:
        model = News
        fields = ('title', 'article', 'created_at', 'updated_at', 'created_by', 'updated_by', 'comments',)

