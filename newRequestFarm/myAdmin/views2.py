# coding='utf8'




# Create your views here.
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# from config.globals import debugLogger
from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializer import BookInfoSerializer
from . import views2

from newRequestFarm import settings
from config.globals import debugLogger


from .models import BookInfo
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


class BookListAPIView(APIView):
    def get(self, request):
        queryset = BookInfo.objects.all()
        # 构建序列化器
        serializer = BookInfoSerializer(queryset,many=True)
        # serializer.data
        resp = json.dumps(serializer.data)
        return Response(resp)
from rest_framework import mixins

# 查询列表集
class BookListGenaricAPIView(mixins.ListModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    def get(self, request):
        # 数据查询
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

# 查询单一的
class BookDailtGenaricAPIView(GenericAPIView):
    queryset = BookInfo.objects .all()
    def get(self, request, pk):
        book = self.get_object()