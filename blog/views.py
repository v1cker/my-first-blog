from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from haystack.forms import SearchForm


def full_search(request):
    """全局搜索"""
    keywords = request.GET['q']
    # 搜索的关键词为用户输入的变量q，该变量是通过前端页面获取的，templates/blog/base.html中32行代码
    sform = SearchForm(request.GET)
    # 搜索表单
    posts = sform.search()
    # 定义搜索对象
    return render(request, 'blog/post_search_list.html',
                  {'posts': posts, 'list_header': '关键字 \'{}\' 搜索结果'.format(keywords)})
    # 返回结果到blog/post_search_list.html页面中，返回个是入上行代码

# Create your views here.
def post_list(request):
    """博文列表"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # 定义全部的博文对象
    paginator = Paginator(posts, 4)
    # 设置分页参数，当前设置为4页
    page = request.GET.get('page')
    # 当前页面定义为用户请求访问的页面
    try:
        posts = paginator.page(page)
        # 显示的所有博文对象为用户所选取的页面，就是分页了以后有好多页面，显示的那页中的4个博文
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    # 以上代码为抛出异常情况，是分页函数固定写法
    return render(request, 'blog/post_list.html', {'posts': posts})
    # 返回博文对象到blog/post_list.html中，是用户选取的那4个

def post_detail(request, pk):
    """博文详细"""
    post = get_object_or_404(Post, pk=pk)
    # pk可以理解为文章编号，文章内容为带有编号的文章
    # 404那个函数是Django内置函数，意思如果没有获取正确的编号即为空对象时，则返回404页面
    return render(request, 'blog/post_detail.html', {'post': post})
    # 返回博文信息到博文详细页面

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_new(request):
    """创建新的博文"""
    if request.method == "POST":
        # 设置用户提交新的博文请求方式为POST请求方式
        form = PostForm(request.POST)
        if form.is_valid():
        # 如果表单有效，则保存表单内容和作者，并返回博文详细的页面
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    # 如果无效，则继续返回到编辑的页面

# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    """文章编辑功能"""
    post = get_object_or_404(Post, pk=pk)
    # pk可以理解为文章编号，文章内容为带有编号的文章
    # 404那个函数是Django内置函数，意思如果没有获取正确的编号即为空对象时，则返回404页面
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        # 设置表单提交方式为POST提交方式
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
        # 如果表单有效，则保存表单，自动提交关闭，保存作者，并返回文章详细页面
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    # 否则，则返回文章编辑页面

# def post_draft_list(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
#     return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_draft_list(request):
    """草稿箱功能，显示所有草稿"""
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    # 现实所有博文对象中发布时间为空的
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
    # 将这些博文返回到草稿箱列表页面

@login_required
def post_publish(request, pk):
    """博文提交功能"""
    post = get_object_or_404(Post, pk=pk)
    # pk可以理解为文章编号，文章内容为带有编号的文章
    # 404那个函数是Django内置函数，意思如果没有获取正确的编号即为空对象时，则返回404页面
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)
    # 将文章发布，并调取views下的post_detail函数

def post_remove(request, pk):
    """文章删除功能"""
    post = get_object_or_404(Post, pk=pk)
    # pk可以理解为文章编号，文章内容为带有编号的文章
    # 404那个函数是Django内置函数，意思如果没有获取正确的编号即为空对象时，则返回404页面
    post.delete()
    return redirect('blog.views.post_list')
    # 将文章删除，并调取views下的post_list函数
