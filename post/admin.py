#coding=utf-8
from django.contrib import admin

# Register your models here.
from post.models import *

# 在后台页面修改显示内容，显示帖子名称和发帖时间
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','createtime')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin)
