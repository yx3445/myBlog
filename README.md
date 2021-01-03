## 一、环境配置
1. VSCode  下载，安装python ，chinese，path intellisence，npm ，npm intellisence   ,Vetur，Vue3 Snippets ,vscode-icons，live server 这些插件

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX   https://www.dcloud.io/hbuilderx.html

4. 安装小程序开发工具   https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html


## 二、安装git：https://git-scm.com/；

1. 创建远程仓库myBlog

2. 初始化本地仓库，也就是在本地的myBLog文件夹下执行：`git init`，执行完后会创建一个.git的隐藏文件

3. 远程仓库和本地仓库进行关联：`git remote add origin "你的远程仓库地址"`

4. 如果出现错误，ssh没有创建

5. 先去创建密钥：`ssh-keygen` ，一路enter，生成密钥

6. 查看生成的密钥   `cat ~/.ssh/id_rsa.pub`，将密钥写入到github上的settings下的SSH and GPG keys下

7. 推送四步骤：

   git status           查看发生变化的文件

   git add .             追踪所有发生变化的文件

   git commit -m "备注"    提交到本地仓库

   git push -u origin master  第一次提交  到远程仓库

   git push  之后的提交

   

## 三、创建myBlog项目

1. 空文件夹下，执行 `django-admin startproject myBlog`;
2. 给myBlog创建虚拟环境，使用：`python -m venv env`
3. 进入到虚拟环境，windows下：`.\\env\\Scrtipst\\activate`;
4. 退出虚拟环境，windows下：`deactivate`；
5. 使用VSCode打开myBlog，执行：`python manage.py startapp articles`





## 四、创建articles的models

1. 打开articles的models.py编辑上以下内容；

2. ~~~python
   from django.db import models
   from django.contrib.auth.models import User
   
   # Create your models here.
   class Articles(models.Model):
       title = models.CharField(max_length=128,verbose_name='文章标题')
       author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='文章作者')
       img = models.ImageField(upload_to="",blank=True,verbose_name='文章插图')
       abstract = models.TextField(verbose_name='文章摘要')
       content = models.TextField(verbose_name='文章内容')
       visited = models.IntegerField(default=0,verbose_name='文章访问量')
       created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
       modified_at = models.DateTimeField(auto_now=True,verbose_name='修改时间')
   
       # 源编程起别名排序
       class Meta:
           verbose_name = '文章'
           verbose_name_plural = verbose_name
           ordering = ('-created_at',)
   
   
       def __str__(self):
           return self.title
   
   ~~~

3. 再打开articles的admin.py编辑上以下内容；

4. ~~~python
   from django.contrib import admin
   from .models import Articles
   
   class ArticlesAdmin(admin.ModelAdmin):
       # 表头
       list_display=('title','author','img','abstract','visited','created_at')
       # 搜索
       search_fields=('title','author','abstract','content')
       #筛选
       list_filter=list_display
   
   
   admin.site.register(Articles,ArticlesAdmin)
   ~~~

5. python manage.py createsuperuser 创建管理员账户密码

6. python manage.py runserver启动项目

   

