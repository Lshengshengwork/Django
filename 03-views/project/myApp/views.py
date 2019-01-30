#coding=utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse('来了老弟')
    return render(request,'myApp/index.html')



def attribute(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    return HttpResponse('attribute')

#GET
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + "  " + b + "  " +c)


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1 + "  " + a2 + "  " +c)


def showregister(request):
    return render(request, 'myApp/register.html')

#POST
def register(request):
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    age = request.POST.get('age')
    habby = request.POST.get('habby')
    return HttpResponse("name:%s; gender: %s ; age: %s ; habby: %s"%(name,gender,age,habby))


# response
def showresponse(request):
    res = HttpResponse()
    res.content = b'hello'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    # print(res.content-type)
    return res


def cookietest(request):
    res = HttpResponse()
    # 获取cookie
    getcookie = request.COOKIES
    res.write("<h1>"+getcookie['cookie-name'] +"</h1>")
    # 设置cookie
    cookie = res.set_cookie("cookie-name","1234a")
    return res


# 重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    # return HttpResponseRedirect('/myapp/redirect2')
    #还有一种简单的写法，推荐
    return redirect('/myapp/redirect2')

def redirect2(request):
    return HttpResponse("我是重定向后的视图")




def main(request):
    # 取session
    username = request.session.get('name',"游客")
    return render(request, 'myApp/main.html',{"username":username})

def login(request):
    return render(request, 'myApp/login.html')

def showmain(request):
    username = request.POST.get('username')
    # 存储session
    request.session['name'] = username
    return redirect('/myapp/main')















