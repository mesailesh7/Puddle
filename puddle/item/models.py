from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    # by default django will put Categorys in name in order to change it we use below
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name',]

    # by default django puts the name as object so to change it
    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='items',blank=True,null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name





