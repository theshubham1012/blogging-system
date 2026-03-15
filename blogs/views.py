from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts':posts,
        'category':category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, blog_slug):
    singleBlog = get_object_or_404(Blog, slug=blog_slug, status='Published')
    if request.method=='POST':
        new_comment = Comment()
        new_comment.user = request.user
        new_comment.blog = singleBlog
        new_comment.comment = request.POST['comment']
        new_comment.save()
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=singleBlog)
    comment_count = comments.count()
    context = {
        'single_blog' : singleBlog,
        'comments' : comments,
        'comment_count' : comment_count, 
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published") ##__icontains used to search a part or letters in a sentence or etc.
    context = {
        'blogs': blogs,
        'keyword' : keyword,
    } 
    return render(request, 'search.html', context)

