from django.contrib import admin

from .models import Post


# Register your models here.
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on']

    search_fields = ['title']


admin.site.register(Post, PostAdmin)
