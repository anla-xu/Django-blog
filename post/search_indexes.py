#coding=UTF-8
from  haystack import indexes
from post.models import *

#注意格式(模型类名+Index)
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    '''
    全文检索配置，文件名必须为serach_indexes，搜索引擎底层会检索这个文件
    '''
    text = indexes.CharField(document=True, use_template=True)#默认字段

    #给title,content设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    # 重写父类的方法
    def get_model(self):
        return Post

    # 检索结果
    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-createtime')