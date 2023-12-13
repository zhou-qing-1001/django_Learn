from django.db import models

"""
继承models.Model
自动添加主键(id)
字段

    字段名=model.类型(选项)
    
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
# Create your models here.
