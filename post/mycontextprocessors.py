#coding=utf-8
from django.db.models import Count

from .models import *

def m_right_cate(request):
    # 定义全局上下文，获得帖子类别以及数量，按降序排列
    rpost_kind = Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')

    # 文章归档
    # file_time = Post.objects.dates('createtime','month',order='DESC')
    from django.db import connection

    cursor = connection.cursor()# DATE_FORMAT日期转字符串
    cursor.execute("SELECT createtime,COUNT(*) FROM (SELECT DATE_FORMAT(createtime,'%Y-%m') createtime FROM blog_post) c GROUP BY createtime ORDER BY createtime")
    file_time = cursor.fetchall()  # 得到一个元组(('2020-04',3),('2020-05',5))

    # 近期文章
    recent_posts = Post.objects.all().order_by('-createtime')[:5]
    return {'r_postkind':rpost_kind,'r_recentposts':recent_posts,'r_filetime':file_time}