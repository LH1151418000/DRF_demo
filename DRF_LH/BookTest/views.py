from django.shortcuts import render
from django.views import View
from .models import BookInfo
from django.http import JsonResponse
import json
# Create your views here.


class BooksView(View):

    # 1、获取多条/列表数据
    # 请求方式：GET
    # 请求路径：/books/
    # 请求参数：无
    # 响应数据：json格式

    def get(self, request):
        books = BookInfo.objects.all()

        book_list = []
        for book in books:
            book_list.append({
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'is_delete': book.is_delete,
                'image': book.image.url or ''
            })
        return JsonResponse(book_list, safe=False)

    # 2、新建一本书
    # 请求方式：POST
    # 请求路径：/books/
    # 请求参数：json格式
    # 响应数据：json格式

    def post(self, request):
        # 提取参数
        book_info = json.loads(request.body)

        # 校验参数
        btitle = book_info.get('btitle')
        bpub_date = book_info.get('bpub_date')
        if not all([btitle, bpub_date]):
            return JsonResponse({'errmsg': '缺少必传字段'}, status=400)
        if len(btitle) > 20:
            return JsonResponse({'errmsg': '超出范围'}, status=400)

        # 新建资源
        book = BookInfo.objects.create(**book_info)

        # 返回响应
        return JsonResponse({
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'is_delete': book.is_delete,
        })


class BookView(View):

    # 3、指定id的书
    # 请求方式：GET
    # 请求路径：/books/<pk>/
    # 请求参数：路径参数pk
    # 响应数据：json格式

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return JsonResponse({'errmsg': '资源不存在'}, status=400)

        book_dict = {
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'is_delete': book.is_delete,
            'image': book.image.url or ''
        }

        return JsonResponse(book_dict)

    def put(self, request, pk):
        book_info = json.loads(request.body)
        btitle = book_info.get('btitle')
        bpub_date = book_info.get('bpub_date')
        if not all([btitle, bpub_date]):
            return JsonResponse({'errmsg': '缺少必传字段'}, status=400)
        if len(btitle) > 20:
            return JsonResponse({'errmsg': '超出范围'}, status=400)

        BookInfo.objects.filter(pk=pk).update(**book_info)
        book = BookInfo.objects.get(pk=pk)
        return JsonResponse({
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'is_delete': book.is_delete
        })

    def delete(self, request, pk):
        book = BookInfo.objects.get(pk=pk)
        book.delete()
        return JsonResponse({}, status=204)