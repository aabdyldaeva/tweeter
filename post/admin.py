from django.contrib import admin
from .models import Tweet, Comment, CommentLikeDislike, TweetLikeDislike

admin.site.register(Tweet)
admin.site.register(TweetLikeDislike)
admin.site.register(Comment)
admin.site.register(CommentLikeDislike)