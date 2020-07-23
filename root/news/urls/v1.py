from django.urls import path

from news.views import NewsListCreateAPIView, NewsRetrieveUpdateApiView

urlpatterns = [
    path('news/', NewsListCreateAPIView.as_view(), name='news-list-create-api'),
    path('news/<int:id>/', NewsRetrieveUpdateApiView.as_view(), name='news-get-update-api'),

]
