from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'location', 'photo',)
        # 创建文章标题，内容，地点，图片四个表单框


 # 表单文件，创建文章编辑的那个表单，调用Django的内置表单模块进行创建。
