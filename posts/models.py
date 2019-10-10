from django.db import models
from django.utils.html import format_html
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=50,unique=True,db_index=True)
    description=models.TextField()
    status=models.BooleanField(default=1,db_index=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

        
    def status_view(self):
        if self.status==1:
            status="Active"
            color="Green"
        else:
            status="Inactive"
            color="Red"
        return format_html(
            '<span style="color:{};">{}</span>',
            color,
            status,
        )
    def action(self):
        return format_html(f'<a class="btn" href="/admin/posts/category/{self.pk}/change/">Edit</a>&nbsp;<a class="btn" href="/admin/posts/category/{self.pk}/delete/">Delete</a>', self.pk)



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"


class Posts(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
    title=models.CharField(max_length=50,unique=True,db_index=True)
    slug=models.SlugField(unique=True)
    short_description=models.CharField(max_length=100)
    long_description=models.TextField()
    status=models.BooleanField(default=1,db_index=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

        
    def status_view(self):
        if self.status==1:
            status="Active"
            color="Green"
        else:
            status="Inactive"
            color="Red"
        return format_html(
            '<span style="color:{};">{}</span>',
            color,
            status,
        )
    def action(self):
        return format_html(f'<a class="btn" href="/admin/posts/posts/{self.pk}/change/">Edit</a>&nbsp;<a class="btn" href="/admin/posts/posts/{self.pk}/delete/">Delete</a>', self.pk)



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"