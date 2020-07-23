from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from comment.models import Comment
from comment.serializers import CommentSerializer
from comment.permissions import IsOwnerOrReadOnly


class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(usr=req.user, )


class CommentRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()
