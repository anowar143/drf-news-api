from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from news.models import News
from news.serializers import NewsSerializer
from news.permissions import IsOwnerOrReadOnly


class NewsListCreateAPIView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, updated_by=self.request.user,)


class NewsRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    queryset = News.objects.filter()
    serializer_class = NewsSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()
