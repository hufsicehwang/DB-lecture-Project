# Generated by Django 3.2.8 on 2021-12-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, verbose_name='작성자')),
                ('movieNm', models.TextField(verbose_name='movieNmEn')),
                ('review', models.CharField(max_length=1024, verbose_name='리뷰')),
                ('star', models.IntegerField(max_length=10, verbose_name='별점')),
                ('open', models.CharField(max_length=10, verbose_name='게시판 공개여부')),
                ('writed_date', models.DateTimeField(auto_now_add=True, verbose_name='작성 날짜')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=128, verbose_name='작성자')),
                ('movieNm', models.TextField(verbose_name='movieNmEn')),
                ('review', models.CharField(max_length=1024, verbose_name='리뷰')),
                ('star', models.IntegerField(max_length=10, verbose_name='별점')),
                ('open', models.CharField(max_length=10, verbose_name='게시판 공개여부')),
                ('writed_date', models.DateTimeField(auto_now_add=True, verbose_name='작성 날짜')),
            ],
        ),
    ]
