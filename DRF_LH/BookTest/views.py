from django.shortcuts import render
from django.views import View
from .models import BookInfo
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import *
import json

from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.http import JsonResponse


class BooksAPIView(APIView):

    def get(self, request):

        # 获取查询字符串参数
        # request.query_params等价于request.GET
        # print(request.query_params)

        books = BookInfo.objects.all()
        bs = BookInfoModelSerializer(books, many=True)

        # return JsonResponse(bs.data, safe=False)
        return Response(data=bs.data, status=HTTP_200_OK)

    def post(self, request):
        # json_data = json.loads(request.body)
        # 获取请求体数据(表单/json)
        book_info = request.data

        bs = BookInfoModelSerializer(data=book_info)
        if not bs.is_valid():
            return Response(data={'errmsg': '校验错误'}, status=HTTP_400_BAD_REQUEST)

        bs.save()
        return Response(data=bs.data, status=HTTP_201_CREATED)


class BookAPIView(APIView):
    # 返回单一数据
    # GET + /books/<pk>/
    def get(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        bs = BookInfoModelSerializer(book)
        return Response(data=bs.data)

    # 删除单一数据
    # DELETE + /books/<pk>/
    def delete(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        book.delete()
        return Response(data=None, status=HTTP_204_NO_CONTENT)

    # 全更新
    # PUT + /books/<pk>/
    def put(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        book_info = request.data
        bs = BookInfoModelSerializer(book, data=book_info)
        if not bs.is_valid():
            return Response(bs.errors, status=HTTP_400_BAD_REQUEST)

        bs.save()
        return Response(data=bs.data, status=HTTP_201_CREATED)

    # 部分更新
    def patch(self, request, pk):
        book = BookInfo.objects.get(pk=pk)

        # 部分校验，必要字段传则校验，不传则不校验
        # partial = True 则为部分校验 默认为False
        bs = BookInfoModelSerializer(book, request.data, partial=True)
        if not bs.is_valid():
            return Response(bs.errors, status=HTTP_400_BAD_REQUEST)

        bs.save()
        return Response(bs.data, status=HTTP_201_CREATED)

# Create your views here.

#
# class BooksView(View):
#
#     # 1、获取多条/列表数据
#     # 请求方式：GET
#     # 请求路径：/books/
#     # 请求参数：无
#     # 响应数据：json格式
#
#     def get(self, request):
#         books = BookInfo.objects.all()
#
#         book_list = []
#         for book in books:
#             book_list.append({
#                 'btitle': book.btitle,
#                 'bpub_date': book.bpub_date,
#                 'bread': book.bread,
#                 'bcomment': book.bcomment,
#                 'is_delete': book.is_delete,
#                 'image': book.image.url or ''
#             })
#         return JsonResponse(book_list, safe=False)
#
#     # 2、新建一本书
#     # 请求方式：POST
#     # 请求路径：/books/
#     # 请求参数：json格式
#     # 响应数据：json格式
#
#     def post(self, request):
#         # 提取参数
#         book_info = json.loads(request.body)
#
#         # 校验参数
#         btitle = book_info.get('btitle')
#         bpub_date = book_info.get('bpub_date')
#         if not all([btitle, bpub_date]):
#             return JsonResponse({'errmsg': '缺少必传字段'}, status=400)
#         if len(btitle) > 20:
#             return JsonResponse({'errmsg': '超出范围'}, status=400)
#
#         # 新建资源
#         book = BookInfo.objects.create(**book_info)
#
#         # 返回响应
#         return JsonResponse({
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'is_delete': book.is_delete,
#         })
#
#
# class BookView(View):
#
#     # 3、指定id的书
#     # 请求方式：GET
#     # 请求路径：/books/<pk>/
#     # 请求参数：路径参数pk
#     # 响应数据：json格式
#
#     def get(self, request, pk):
#         try:
#             book = BookInfo.objects.get(pk=pk)
#         except BookInfo.DoesNotExist:
#             return JsonResponse({'errmsg': '资源不存在'}, status=400)
#
#         book_dict = {
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'is_delete': book.is_delete,
#             'image': book.image.url or ''
#         }
#
#         return JsonResponse(book_dict)
#
#     def put(self, request, pk):
#         book_info = json.loads(request.body)
#         btitle = book_info.get('btitle')
#         bpub_date = book_info.get('bpub_date')
#         if not all([btitle, bpub_date]):
#             return JsonResponse({'errmsg': '缺少必传字段'}, status=400)
#         if len(btitle) > 20:
#             return JsonResponse({'errmsg': '超出范围'}, status=400)
#
#         BookInfo.objects.filter(pk=pk).update(**book_info)
#         book = BookInfo.objects.get(pk=pk)
#         return JsonResponse({
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bread': book.bread,
#             'bcomment': book.bcomment,
#             'is_delete': book.is_delete
#         })
#
#     def delete(self, request, pk):
#         book = BookInfo.objects.get(pk=pk)
#         book.delete()
#         return JsonResponse({}, status=204)
