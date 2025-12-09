from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Added slug for admin
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # Added slug for admin
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    # Added created for admin sorting
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.name