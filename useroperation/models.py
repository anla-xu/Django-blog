from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=100)
    e_mail = models.EmailField(max_length=50,unique=True)

    class Meta:
        db_table = 'user'
        verbose_name_plural = u'用户'

    def __str__(self):
        return u'User:%s' % self.username
