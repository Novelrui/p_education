from django.urls import path
from . import views

# 路由只识别函数视图，而views.BannerListAPIView是类视图，所以要转换
urlpatterns = [
  path(r"banner/", views.BannerListAPIView.as_view()),
]