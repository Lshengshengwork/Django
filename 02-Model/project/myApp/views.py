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

def students2(request):
    # 如果没有找到符合条件的对象，会引发"模型类.DoesNotExist"异常
    # 如果找到多个对象，会引发"模型类.MultipleObjectsReturned"异常
    # 用try处理就可以
    studentsList = Students.stuObj2.get(sage=55)
    return HttpResponse("laile")


#分页显示学生
def stupage(request,page):
    #  1-5   5-10   10-15
    #   1     2       3
    #  根据规律算得page
    page = int(page)
    studentsList = Students.stuObj2.all()[(page-1)*5:page*5]
    return render(request, 'myApp/students.html', {'students': studentsList})

# 比较运算符运用之：  查询条件的使用
from django.db.models import Max,Min,Q
def studentsearch(request):
    # studentsList = Students.stuObj2.filter(sname__contains="李")   # 包含的使用(contains)
    # studentsList = Students.stuObj2.filter(sname__startswith="李")   # 查询以李开头的数据
    # studentsList = Students.stuObj2.filter(pk__in=[2,4,5])   #把id等于 2 4 5 的值查询出来
    # studentsList = Students.stuObj2.filter(sage__gte=30)   #把年龄大于等于30的给查询出来
    # studentsList = Students.stuObj2.filter(lastTime__year=2017)   #根据最后修改时间是2017年的值全部查询出来
    studentsList = Students.stuObj2.filter(Q(pk__lte=3) | Q(sage__gt=40))   #Q解决或的关系，这个是查询id小于等于3或者年龄大于40的值
    grade = Grades.objects.filter(students__scontend__contains='詹姆斯')   #描述中带有‘詹姆斯’这三个字的数据是属于哪个班级的
    print(grade)
    maxAge = Students.stuObj2.aggregate(Max('sage'))
    print(maxAge)
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


from django.db.models import F,Q
def grades(request):
    g = Grades.objects.filter(gboynum__gt=F('ggirlnum'))
    print(g)
    return HttpResponse("ooookkk")









