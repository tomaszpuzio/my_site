from django.contrib import admin
from .models import Author, Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "author", "excerpt", "date")

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)