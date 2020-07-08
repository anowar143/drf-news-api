from django.urls import path

from comment.views.comment import CommentListCreateAPIView, CommentRetrieveUpdateApiView

urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create-api'),
    path('comments/<int:id>/', CommentRetrieveUpdateApiView.as_view(), name='comment-get-update-api'),

]
