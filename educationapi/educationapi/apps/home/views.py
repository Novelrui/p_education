from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializer import BannerModelSerializer
from educationapi.settings import constant
class BannerListAPIView(ListAPIView): # 自动导包
  queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("-orders", "-id")[:constant.BANNER_LENGTH] #[:] 切片，对从后台取回的数据进行数量的限制
  serializer_class = BannerModelSerializer
