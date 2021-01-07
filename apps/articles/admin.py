from django.contrib import admin
from .models import Articles,Category,Tag
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

class ArticlesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':AdminMarkdownxWidget},
    }
    # 表头
    list_display=('title','author','img','abstract','visited','created_at')
    # 搜索
    search_fields=('title','author','abstract','content')
    # 筛选
    list_filter=list_display


admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Category,)
admin.site.register(Tag,)