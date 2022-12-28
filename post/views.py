from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS, \
    IsAuthenticated
from rest_framework import views
from rest_framework.response import Response

from .models import Tweet, Comment, TweetLikeDislike, CommentLikeDislike
from .serializers import TweetSerializer, CommentsSerializer
from rest_framework import authentication
from rest_framework import permissions


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif bool(request.user and request.user.is_authenticated):
            return True
        else:
            return False


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeTweetAPIView(views.APIView):
    authentication_classes = authentication.TokenAuthentication
    permission_classes = [ReadOnly]

    def post(self, request, *args, **kwargs):
        tweet_id = kwargs.get('tweet_id')
        author = request.user
        dislike = kwargs.get('like')

        new_like_dislike_tweet = TweetLikeDislike(
            tweet_id=tweet_id,
            author=author,
            is_dislike=dislike
        )
        new_like_dislike_tweet.save()
        return Response(status=200)


class LikeCommentAPIView(views.APIView):
    authentication_classes = authentication.TokenAuthentication
    permission_classes = [ReadOnly]

    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        author = request.user
        dislike = kwargs.get('like')

        new_like_dislike_comment = CommentLikeDislike(
            comment_id=comment_id,
            author=author,
            is_dislike=dislike
        )
        new_like_dislike_comment.save()
        return Response(status=200)
