from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from domo.models import BookInfo
from rest_framework import generics
from rest_framework.views import APIView


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
