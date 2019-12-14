from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=11, db_column='title', verbose_name='书标题')
    bdata = models.DateField(verbose_name='日期')
    bread = models.IntegerField(default=0)  # 阅读量
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除

    def tle(self):    # 单独定义方法，显示要显示的数据
        return self.btitle
    tle.admin_order_field = 'btitle'    # 设置排序功能
    tle.short_description = '书名---'      # 设置书名标题头
    # class Meta:
    #     verbose_name = '图书名'


    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=11,verbose_name='英雄')
    hcomment = models.CharField(max_length=100)
    hgender = models.BooleanField(default=0)
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, verbose_name='书籍')
    def __str__(self):
        return self.hname

class PicTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')  # 上传图片存储数据表

class CaseNumber(models.Model):
    case_number = models.CharField(max_length=20, verbose_name='用编号')
    case_desc = models.CharField(max_length=20,null=True, blank=True, verbose_name='用例描述' )
    def __str__(self):
        return self.case_number
    class Meta:
        verbose_name='用例编号'

class module(models.Model):
    module_name = models.CharField(max_length=20, verbose_name='模块名')
    weight = models.IntegerField(verbose_name='权重')
    modules_case = models.ManyToManyField(CaseNumber, verbose_name='关联用例')
    def __str__(self):
        return self.module_name +' ,' + str(self.weight)
    class Meta:
        verbose_name = '模块'

class ProjectNumber(models.Model):
    project_name = models.CharField(max_length=20,unique=True, verbose_name='项目')
    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name = '任务名'

class ProjectModule(models.Model):
    project_pk = models.ForeignKey(ProjectNumber, on_delete=models.CASCADE,db_index=True, verbose_name='项目名')
    module_pk = models.ForeignKey(module, on_delete=models.CASCADE,  verbose_name='执行模块')
    class Meta:
        verbose_name = '项目表'
    def project_data(self):
        return self.project_pk.project_name
    def project_modules(self):
        return self.module_pk.weight
    project_data.short_description = '项目显示'
    project_modules.short_description = '权重'
    project_modules.admin_order_field = 'module_pk__weight'




