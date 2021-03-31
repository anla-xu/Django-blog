#coding=utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# 类别
from django.urls import reverse

from useroperation.models import User


class Category(models.Model):
    cname = models.CharField(max_length=30,unique=True,verbose_name=u'类别名')

    class Meta:
        db_table='blog_category'
        # 修改后台表名
        verbose_name_plural=u'类别'

    def __str__(self):
        return u'category:%s'%self.cname

# 标签
class Tag(models.Model):
    tname = models.CharField(max_length=20,unique=True,verbose_name=u'标签名')

    class Meta:
        db_table = 'blog_tag'
        verbose_name_plural = u'标签'

    def __str__(self):
        return u'Tag:%s' % self.tname

# 帖子
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,unique=True)
    photo = models.ImageField(upload_to='imgs')
    about = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True,blank=True,config_name='my_config')
    createtime = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'blog_post'
        verbose_name_plural = u'帖子'

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('post:detail', args=[self.id])

    def __str__(self):
        return u'post:%s' % self.title


# 评论
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",verbose_name=u'评论',on_delete=models.CASCADE)
    u_name = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post_comment'
        verbose_name_plural = u'评论'

    def __str__(self):
        return u'post_comment:%s' % self.body

#点赞
class Like(models.Model):
    post = models.ForeignKey(Post,related_name="like",verbose_name=u'点赞',on_delete=models.CASCADE)
    u_name = models.ForeignKey(User, on_delete=models.CASCADE)
    good = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    collection = models.BooleanField(default=False)

    class Meta:
        db_table = 'post_like'
        verbose_name_plural = u'点赞'

    def __str__(self):
        return u'post_like:%s' % self.post

