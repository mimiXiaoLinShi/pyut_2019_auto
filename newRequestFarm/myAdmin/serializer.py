# coding: utf-8
from rest_framework import serializers
from .models import BookInfo

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

class caseSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    case_number = serializers.CharField(label='用例编号', max_length=20, required=False)
    case_desc = serializers.CharField(label='描述', max_length=2, default='')
