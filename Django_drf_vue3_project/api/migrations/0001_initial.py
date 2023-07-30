# Generated by Django 4.2.3 on 2023-07-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='用户名')),
                ('count', models.IntegerField(verbose_name='人数')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, verbose_name='用户名')),
                ('pwd', models.CharField(max_length=64, verbose_name='密码')),
                ('role', models.CharField(choices=[('admin', '管理员'), ('user', '用户'), ('manager', '经理')], default='user', max_length=16, verbose_name='角色')),
            ],
        ),
    ]
