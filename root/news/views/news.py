from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from news.models.news import News
from news.serializers.news import NewsSerializer


class NewsListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user,)


class NewsRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = News.objects.filter()
    serializer_class = NewsSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()