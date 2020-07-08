from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from comment.models.comment import Comment
from comment.serializers.comment import CommentSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(usr=req.user, )


class CommentRetrieveUpdateApiView(RetrieveUpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()
