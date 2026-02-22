from .models import Category, Social

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories)

def get_social(request):
    links = Social.objects.all()
    return dict(links = links)