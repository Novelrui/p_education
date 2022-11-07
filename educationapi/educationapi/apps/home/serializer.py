from rest_framework import serializers
from .models import Banner

class BannerModelSerializer(serializers.ModelSerializer):
  '''轮播广告的序列化器'''
  # 过滤的字段声明

  # 模型序列化器字段声明
  class Meta:
    model = Banner
    fields = ["image_url", "link"]


  # 验证方法

  # 存储数据方法

