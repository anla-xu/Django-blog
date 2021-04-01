# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# 渲染主页面
from post.forms import CommentForm
from post.models import Post, Comment, Like
from django.core.paginator import Paginator
import math

from useroperation.models import User


def queryAll(request, num=1):
    num = int(num)
    # 获取所有帖子信息
    postList = Post.objects.all().order_by('-createtime')

    print(postList)
    perPageList, pageList = fenye(postList, num)
    return render(request, 'index.html', {'postList': perPageList, 'pageList': pageList, 'currentNum': num})


def fenye(postList, num):
    # 创建分页器对象
    pageObj = Paginator(postList, 3)

    # 获取当前页的数据
    perPageList = pageObj.page(num)

    # 生成页码数列表
    # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)
    return perPageList, pageList


# 展示文章
def detail(request, postid):
    post = Post.objects.get(id=postid)
    # 取出点赞数
    likes = Like.objects.filter(post_id=postid, good=True)
    # print("likes:",likes.count())
    # 取出文章评论
    comments = Comment.objects.filter(post=postid)

    # 获取收藏数
    collections = Like.objects.filter(post_id=postid, collection=True)
    # print("收藏数：",collections)
    status = {'like':0,'collect':0}
    # 判断该用户是否点赞收藏
    try:
        obj = Like.objects.get(post=postid, u_name_id=request.session['id'])
        like_status = 0 if not obj.good else 1
        collect_status = 0 if not obj.collection else 1
        status['like'] = like_status
        status['collect'] = collect_status
    except:
        pass
    print(status)
    return render(request, 'postdetail.html',
                  {'post': post, 'comments': comments, 'likes': likes, 'status': status, 'collections': collections})


# 展示同类别的文章
def file_category(request, kind):
    same_fileall = Post.objects.filter(category_id=kind)
    return render(request, 'samecagefile.html', {'same_fileall': same_fileall})


# 展示同一个月的文章

def same_month(request, year, month):
    samemonthpost = Post.objects.filter(createtime__year=year, createtime__month=month)
    return render(request, 'samecagefile.html', {'same_fileall': samemonthpost})


def post_comment(request, post_id):
    print(post_id)
    article = get_object_or_404(Post, id=post_id)
    print(article)
    # 处理 POST 请求
    response = {'st':1}
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            print(new_comment)
            new_comment.post = article
            new_comment.u_name = User.objects.get(id=request.session['id'])
            new_comment.save()
            try:
                obj = Like.objects.get(u_name_id=request.session['id'])
                obj.collection = True
                obj.save()
            except:
                Like.objects.create(u_name_id=request.session['id'],post_id=post_id,collection=True)
            return JsonResponse(response)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")


# 联系作者
def contact(request):
    return render(request, 'contact.html')


# 点赞
def like(request):
    print("进来了")
    try:
        article_id = request.POST.get('article_id')
        # 判断该用户是否点赞
        status = request.POST.get('status')
        print(status,article_id)
        response = {'status': True}
        u_id = User.objects.get(username=request.session['username']).id
        try:
            obj = Like.objects.get(u_name_id=u_id, post_id=article_id)
            if status == 'like':
                if obj.good:
                    response['status'] = False
                    obj.good = False
                    obj.save()
                    print("用户取消点赞")
                else:
                    obj.good = True
                    obj.save()
                    print("用户点赞成功！")
            else:
                if obj.collection:
                    response['status'] = False
                    obj.collection = False
                    obj.save()
                    print("用户取消收藏")
                else:
                    obj.collection = True
                    obj.save()
                    print("用户收藏成功！")
        except:
            if status == 'like':
                    Like.objects.create(post_id=article_id, u_name_id=u_id, good=True)
                    # 生成了赞记录， 然后再来更新页面
            else:
                    Like.objects.create(post_id=article_id, u_name_id=u_id, collection=True)

        return JsonResponse(response)
    except:
        return redirect('useroperation::logining')


# 用户点赞的文章
def mylike(request):
    postList = Like.objects.filter(u_name_id=request.session['id'],good=True).order_by('post_id')
    return render(request, 'userlike.html', {'postList': postList,'tip':'我的点赞：'})


# 用户评论的文章
def mycomment(request):
    postList = Like.objects.filter(u_name_id=request.session['id'],comment=True).order_by('post_id')
    return render(request, 'userlike.html', {'postList': postList,'tip':'我参与的评论：'})


# 用户收藏的文章
def mycollection(request):
    postList = Like.objects.filter(u_name_id=request.session['id'], collection=True).order_by('post_id')
    return render(request, 'userlike.html', {'postList': postList,'tip':'我的收藏：'})


def aboutauthor(request):
    return render(request,'aboutcreate.html')