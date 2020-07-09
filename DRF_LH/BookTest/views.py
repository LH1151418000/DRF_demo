from django.shortcuts import render
from django.views import View
from .models import BookInfo
from django.http import JsonResponse
# Create your views here.


class BooksView(View):

    def get(self, request):
        books = BookInfo.objects.all()

        book_list = []
        for book in books:
            book_list.append({
                'btitle': book.btitle,
                'bpub_date': book.bpub_date
            })

        # 前后端不分离--页面渲染
        # return render(request, 'index.html', context={'book_list': book_list})
        # 前后端分离--仅提供数据
        return JsonResponse(data=book_list, safe=False)
