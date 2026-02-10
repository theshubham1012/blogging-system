from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    # django adds an 's' at the last of admin panel to maki it plural, so to set correct plural name we use Meta
    class Meta:
        verbose_name_plural = 'categories'

    #sets the string reprensentation of the object
    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('Draft', 'DRAFT'),
    ('Published', 'PUBLISHED')
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # on deleting category model related with it will also be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featued_image = models.ImageField(upload_to='uploads/%Y/%M/%D')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=1000)
    status = models.CharField(choices=STATUS_CHOICES, default='Draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title