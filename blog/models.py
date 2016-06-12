from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# 此文件是Django创建数据库模型的文件，在该文件中定义需要用到的数据值。并设置他们的属性。
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    # 作者调取Django的用户，也就是适用Django后台可以登录的用户
    title = models.CharField(max_length=200)
    # 标题，最大长度文200的字符串
    text = models.TextField()
    # 内容，定义为内容文本
    created_date = models.DateTimeField(
            default=timezone.now)
    # 创建时间，时间类型，默认为系统时间
    published_date = models.DateTimeField(
            blank=True, null=True)
    # 发布时间，时间类型，该字段在新建博文的时候可以不填为空，因为不填就会存储在草稿箱中，填了就会发布，因为是发布时间
    # 数据库该值可以为空，
    photo = models.URLField(blank=True)
    # 照片地址，url类型，可以为空不填
    location = models.CharField(max_length=100)
    # 地点，字符串最大长度100

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # 定义一个发布函数，调用该函数时自动获取当时系统时间，并保存

    def __str__(self):
        return self.title
    # 将返回的标题转化为字符串返回
