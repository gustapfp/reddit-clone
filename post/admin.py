from django.contrib import admin
from post.models import Post

# Register your models here.
class ListingPost(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('topic',)
    list_per_page = 10
    ordering = ('title',)


admin.site.register(Post, ListingPost)