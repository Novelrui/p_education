import xadmin
from xadmin import views

class BaseSetting(object):
  """xadmin的基本配置"""
  enable_themes = True
  use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
  """xadmin的全局配置"""
  site_title = "Education CIty" # 设置站点名称
  site_footer = "Education CIty Company Ltd." # 设置站点页脚
  menu_style = "accordion" #设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)

# 轮播图
from .models import Banner
class BannerModelAdmin(object):
  list_display = ["title", "orders", "is_show"]
xadmin.site.register(Banner, BannerModelAdmin)