from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from django import views
from requests import request
from .serializers import CommentSerializer
from .models import Comment


class Users(views.View):
    def get(self, request):
        return HttpResponse("ok")


class CommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CreateCommentView(CreateAPIView):
    serializer_class = CommentSerializer
