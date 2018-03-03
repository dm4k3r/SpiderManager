# Generated by Django 2.0.2 on 2018-02-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lagou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.CharField(max_length=50, verbose_name='网址生成id')),
                ('url', models.CharField(max_length=300, verbose_name='网址')),
                ('company', models.CharField(max_length=200, verbose_name='公司名称')),
                ('position', models.CharField(max_length=200, verbose_name='职位')),
                ('minimum_wage', models.IntegerField(verbose_name='最低工资')),
                ('maximum_wage', models.IntegerField(verbose_name='最高工资')),
                ('location', models.CharField(max_length=50, verbose_name='城市')),
                ('minimum_experience', models.IntegerField(verbose_name='最低工作经验')),
                ('maximum_experience', models.IntegerField(verbose_name='最高工作经验')),
                ('education_requirements', models.CharField(max_length=50, verbose_name='学历要求')),
                ('type', models.CharField(max_length=50, verbose_name='工作类型')),
                ('description', models.TextField(verbose_name='工作内容介绍')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='公司地址')),
                ('publish_time', models.DateField(verbose_name='发布时间')),
                ('status', models.CharField(max_length=50, verbose_name='职位状态')),
                ('crawl_created_time', models.DateTimeField(verbose_name='爬取时间')),
                ('crawl_updated_time', models.DateTimeField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '拉勾网',
            },
        ),
    ]