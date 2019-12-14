from django.contrib import admin

# Register your models here.


# Register your models here.
from django.db.models import Q

from .models import HeroInfo, BookInfo, PicTest, CaseNumber, module, ProjectNumber, ProjectModule

from django.contrib import admin

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bdata', 'tle']  # 商品详情业显示的内容
    list_per_page = 2      # 商品分页数
    actions_on_top = True   # 上部显示属性
    actions_on_bottom = True   # 底部显示属性
    list_filter = ['btitle']   # 用户快速过滤字段
    search_fields = ['btitle']   # 搜索框，用于快速搜索

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hbook']
    action_on_bottom = True

class caseNumberAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            isRepeat = len(CaseNumber.objects.filter(~Q(id=obj.id), case_number=obj.case_number))
            print('isRepeat is ===== %s' % isRepeat)
        else:
            isRepeat = len(CaseNumber.objects.filter(case_number=obj.case_number))
            print('isRepeat is %s' % isRepeat)
        if isRepeat == 0:
            obj.save()
            msg = u'操作成功'
        else:
            msg = u'操作失败'
        self.message_user(request, msg)

    list_per_page = 50
    list_display = ('case_number', 'case_desc')
    list_filter = ['case_number']

class moduleAdmin(admin.ModelAdmin):
    def save_model(self,request, obj, form, change):
        if change:
            isRepeat = len(module.objects.filter(~Q(id=obj.id), module_name=obj.module_name).values())
        else:
            isRepeat = len(module.objects.filter(module_name=obj.module_name).values())

        if isRepeat == 0:
            obj.save()
            msg = u'操作成功'
        else:
            msg = u'操作失败'
        self.message_user(request, msg)
    list_display = ('module_name', 'weight')


class ProjectModuleAdmin(admin.ModelAdmin):
    def show_btitel(self,obj):
        return obj.project_pk.project_name
    def show_btitle2(self, obj):
        return obj.module_pk.module_name

    def show_btitle3(self, obj):
        return obj.module_pk.weight

    list_display = ('show_btitel', 'show_btitle2', 'show_btitle3', 'project_data', 'project_modules')
    action_on_bottom = True
    # list_filter = ['project_data']
    search_fields = ['project_modules']
    # fields = ['project_modules']
    pass

class ProjectNumberAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            isRepeat = len(ProjectNumber.objects.filter(~Q(id=obj.id), project_name=obj.project_name).values())
        else:
            isRepeat = len(ProjectNumber.objects.filter(project_name=obj.project_name).values())

        if isRepeat == 0:
            obj.save()
            msg = u'操作成功'
        else:
            msg = u'操作失败'
        self.message_user(request, msg)
    list_display = ('project_name',)


admin.site.register(ProjectNumber, ProjectNumberAdmin)
admin.site.register(ProjectModule, ProjectModuleAdmin)
admin.site.register(module, moduleAdmin)
admin.site.register(CaseNumber, caseNumberAdmin)



admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(PicTest)