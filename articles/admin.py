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