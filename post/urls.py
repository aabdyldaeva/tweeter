from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('tweet', views.TweetViewSet)
router.register('comment', views.CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('tweet/<int:tweet_id>/<int:dislike>/', views.LikeTweetAPIView.as_view()),
]