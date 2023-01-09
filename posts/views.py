import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import views
from rest_framework import authentication

from .models import Tweet, Comment, Likes
from .serializers import TweetSerializer, CommentSerializer, LikeSerializer
# from .my_generics import MyListCreateAPIView
from .my_generics import MyAPIView, \
    ListMixinAPI, CreateMixinAPI, \
    RetrieveMixinAPI, UpdateMixinAPI, \
    DeleteMixinAPI


class TweetCreateListView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [
        authentication.BasicAuthentication,
        authentication.TokenAuthentication
    ]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer


class CommentListCreateAPIView(ListMixinAPI, CreateMixinAPI, MyAPIView):
    serializer_class = CommentSerializer
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentRetrieveUpdateDestroyAPIView(RetrieveMixinAPI,
                                          DeleteMixinAPI,
                                          UpdateMixinAPI,
                                          MyAPIView):
    serializer_class = CommentSerializer
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class LikeCreateListView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer


class LikeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
