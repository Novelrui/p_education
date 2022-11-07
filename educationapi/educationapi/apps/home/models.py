from django.db import models

# Create your models here.
class Banner(models.Model):
  """轮播广告图模型"""
  # 模型字段
  title = models.CharField(max_length = 500, verbose_name = "adtitle")
  link = models.CharField(max_length = 500, verbose_name = "adlinks")
  image_url = models.CharField(max_length = 255, verbose_name = "picture")
  remark = models.TextField(verbose_name = "tips")
  is_show = models.BooleanField(default=False, verbose_name = "show or not show")
  orders = models.IntegerField(default=1, verbose_name = "sort")
  is_deleted = models.BooleanField(default=False, verbose_name = "delete or not delete")

  # 表信息声明
  class Meta:
    db_table = "p_educate_banner"
    verbose_name = "轮播广告"
    verbose_name_plural = verbose_name

  #自定义方法 [自定义字段或自定义工具方法]
  def __str__(self):
    return self.title
