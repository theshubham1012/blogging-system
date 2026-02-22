from django.shortcuts import render
from blogs.models import About, Blog

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published') #orderby('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)