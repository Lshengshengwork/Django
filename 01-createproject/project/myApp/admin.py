from django.contrib import admin

# Register your models here.
from .models import Grades,Students

# 注册


class StudentInfo(admin.TabularInline):  # StackedInline 这种也可以，只是格式不一样
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #添加 、 修改 页属性
    fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    # fieldsets = [
    #     ("num",{"fields":['ggirlnum','gboynum']}),
    #     ("base",{"fields":['gname','gdate','isDelete']}),
    # ]

admin.site.register(Grades,GradesAdmin)

@admin.register(Students)
class StudentAamin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = '性别'

    list_display = ['pk','sname',gender,'sage','scontend','isDelete']
    list_per_page = 10
    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False

# admin.site.register(Students,StudentAamin)