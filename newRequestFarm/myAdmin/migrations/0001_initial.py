# Generated by Django 2.1.1 on 2019-12-14 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(db_column='title', max_length=11, verbose_name='书标题')),
                ('bdata', models.DateField(verbose_name='日期')),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CaseNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=20, verbose_name='用编号')),
                ('case_desc', models.CharField(blank=True, max_length=20, null=True, verbose_name='用例描述')),
            ],
            options={
                'verbose_name': '用例编号',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=11, verbose_name='英雄')),
                ('hcomment', models.CharField(max_length=100)),
                ('hgender', models.BooleanField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAdmin.BookInfo', verbose_name='书籍')),
            ],
        ),
        migrations.CreateModel(
            name='module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=20, verbose_name='模块名')),
                ('weight', models.IntegerField(verbose_name='权重')),
                ('modules_case', models.ManyToManyField(to='myAdmin.CaseNumber', verbose_name='关联用例')),
            ],
            options={
                'verbose_name': '模块',
            },
        ),
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='booktest/')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAdmin.module', verbose_name='执行模块')),
            ],
            options={
                'verbose_name': '项目表',
            },
        ),
        migrations.CreateModel(
            name='ProjectNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20, unique=True, verbose_name='项目')),
            ],
            options={
                'verbose_name': '任务名',
            },
        ),
        migrations.AddField(
            model_name='projectmodule',
            name='project_pk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myAdmin.ProjectNumber', verbose_name='项目名'),
        ),
    ]
