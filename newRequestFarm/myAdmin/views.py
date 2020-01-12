# coding='utf8'


import base64

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.serializers import json
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# from config.globals import debugLogger
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.response import Response

from config.globals import debugLogger



from datetime import date
import sys
# sys.setdefaultencoding('utf8')

# 分页显示
NumberColumns= 15

# 当页面编辑新增删除后拿的全部数据，返回第一页的数据
def get_firstpage(dataModel):
    data_list = dataModel.objects.all().order_by('-id')
    debugLogger.info('data_list is %s' % data_list)
    paginator = Paginator(data_list, NumberColumns)
    contacts = paginator.page(1)
    return contacts


# 当页面编辑新增删除后拿的全部数据，返回第一页的数据，根据登陆用户过滤数据
def get_firstPagefilterdata(dataModel, filiterdata):
    data_list = dataModel.objects.all().order_by('-id')
    # 将数据在根据登陆用户过滤一层


def get_index(request):
    return render(request, 'index.html')


# 登陆验证

def login_action(request):
    if request.method == 'POST':
        userName = request.POST.get('form-username')
        passWord = request.Post.get('form-password')

        user = auth.autherticate(username = userName, password = passWord)
        debugLogger.info('login_action function user is %s' % user)
        if user != None:
            auth.login(request, user)
            request.session["Username"] = userName
            # 更新密码
            User.objects.filter(username=userName).update(pwd=base64.b64encode(bytes(passWord,'utf-8')))
            return HttpResponseRedirect("/first_page")
        else:
            return render(request, "index.html", {"error": "userName or passWord is error"})


@login_required
def first_page(request):
    try:
        userName = request.session['Username']
        return render(request, "first_page.html", {"Username": userName})
    except:
        return render('index.html')












































# def index(request):
#     template = loader.get_template('adminTemplates/index.html')
#     str = '%s,%s' % (request.path, request.encoding)
#     print(str)
#     # request.session['h1'] = 'hello'
#     request.session.flush()
#     context = {'title':'图书列表','list': range(10)}
#     # return HttpResponse(template.render(context))
#     return render(request, 'adminTemplates/index_old.html', context)


def indexBook(request, city, year):
    bookInfo = BookInfo.objects.all()
    return render(request, 'adminTemplates/indexBook.html', {'bookInfo': bookInfo})

def create(request):
    book=BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bdata = date(1995,12,30)
    book.save()
    #转向到首页
    return redirect('/indexbook/')

def my_decorator(view_func):
    def wrapper(request,  *args, **kwargs):

        print('装饰器被调用')
        return view_func( request, *args, **kwargs)
        return wrapper

# 使用扩展类
class BaseView(View):
    @classmethod
    def as_view(cls,*args, **kwargs):
        # 添加装饰器
        view = my_decorator(super().as_view(*args, **kwargs))
        return view

class HeroInfo(View):
    def get(self, request, dir):
        str = '%s,%s' % (request.path, request.encoding)
        print(str)
        # book = BookInfo.objects.get(id=int(dir))
        # print('------------', book)
        # bookObj = book.heroinfo_set.all()
        # print(bookObj)
        # return render(request, 'adminTemplates/indexHero.html', {'bookObj': bookObj})
        return HttpResponse('45555555555')


# class HeroInfo(View):
#     @method_decorator(my_decorator)
#     def dispath(self, request, *args, **kwargs):    # 重写dispath方法
#         super().dispath(request, *args, **kwargs)

    # @method_decorator(my_decorator)      # 只对get方法加装饰器
    # def get(self, request, dir):
    #     str = '%s,%s' % (request.path, request.encoding)
    #     print(str)
    #     # book = BookInfo.objects.get(id=int(dir))
    #     # print('------------', book)
    #     # bookObj = book.heroinfo_set.all()
    #     # print(bookObj)
    #     # return render(request, 'adminTemplates/indexHero.html', {'bookObj': bookObj})
    #     return HttpResponse('45555555555')


#逻辑删除指定编号的图书
def delete(request, id):
    book=BookInfo.objects.get(id=int(id))
    book.delete()
    #转向到首页
    return redirect('/indexbook/')

# 通过请求参数来返回相应的模板
def show_reqarg(request):
    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')
        c = request.GET.get('c')
        return render(request, 'adminTemplates/show_getarg.html', {'a': a, 'b': b, 'c': c})
    else:
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        hobbys = request.POST.getlist('hobby')
        return render(request, 'adminTemplates/show_postarg.html', {'name':name, 'gender':gender, 'hobbys':hobbys})




#-------------------------------------------------------------------------------
from myAdmin.serializer import caseSerializer
from rest_framework.generics import GenericAPIView
from .models import BookInfo, CaseNumber


class caseList(GenericAPIView):
    queryset = CaseNumber.objects.all()
    serializer_class = caseSerializer
    # def get(self,request, pk):
    #     self.lookup_field = 'case_name'
    #     case = self.get_object()
    #     serializer = self.get_serializr(case)
    #     return Response(serializer.data)

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serilizer = self.get_serializer(queryset, many=True)

        return Response({'data': serilizer.data}, template_name='booktest/pic_pload.html')