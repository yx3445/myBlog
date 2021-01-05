# Generated by Django 3.1.4 on 2021-01-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='文章分类', max_length=128, verbose_name='文章分类')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='文章标签', max_length=128, verbose_name='文章标签')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(to='articles.Category', verbose_name='文章分类'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tag',
            field=models.ManyToManyField(to='articles.Tag', verbose_name='文章标签'),
        ),
    ]