from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from django.http.response import HttpResponse
import logging
logger = logging.getLogger("django")
from rest_framework import status


def custom_exception_handler(exc, context):
  """
  param exec: 本次请求发生的异常信息
  param context: 本次请求发送异常的执行上下文 【本次请求的request对象，异常发送的时间，行号等】
  return
  """
  response = exception_handler(exc, context)

  if response is None:
    '''要么程序没出错，要么出错了django或者restframework不识别'''
    view = context["view"]
    if isinstance(exec, DatabaseError):
      # 数据库异常
      logger.error('[%s] %s' % (view, exec))
      response = Response({'message':"服务器内部错误"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
  return response