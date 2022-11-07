from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Banner
from .serializer import BannerModelSerializer
class BannerListAPIView(ListAPIView): # 自动导包
  queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("-orders", "-id")
  serializer_class = BannerModelSerializer
