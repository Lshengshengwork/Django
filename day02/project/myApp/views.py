from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse('来了老弟')
    return render(request,'myApp/index.html')


from .models import Students,Grades
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request,'myApp/students.html',{'students':studentsList})

def addstudents(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("李易峰",29,True,grade,"我是李易峰","2019-1-20","2019-1-20")
    stu.save()
    return HttpResponse("来了，老弟")



def addstudents2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("薛之谦",31,True,grade,"我是薛之谦","2019-1-20","2019-1-20")
    stu.save()
    return HttpResponse("来了，老弟")