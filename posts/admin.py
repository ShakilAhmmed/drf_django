from django.contrib import admin
from .models import Category,Posts


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','description','status_view','action']

class PostsAdmin(admin.ModelAdmin):
    list_display=['category','title','slug','short_description','status_view','action']
    list_display_links=['title']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Posts,PostsAdmin)