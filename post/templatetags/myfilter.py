#coding=utf-8
# 自定义富文本过滤器，使文件以Markdown的形式展示
from django.template import Library

register = Library()
@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)
@register.filter
def splits(value):
    return value[-2:]