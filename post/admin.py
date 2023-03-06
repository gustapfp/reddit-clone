from django.contrib import admin
from post.models import Post, Comment

# Register your models here.
class ListingPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic')
    list_display_links = ('id', 'title', 'topic')
    search_fields = ('title', )
    list_filter = ('topic',)
    list_per_page = 10
    ordering = ('title',)


admin.site.register(Post, ListingPost)


class ListingComment(admin.ModelAdmin):
    list_display = ('id', 'title', 'post')
    list_display_links = ('id', 'title', 'post')
    search_fields = ('title', )
    list_filter = ('post',)
    list_per_page = 10
    ordering = ('title',)
admin.site.register(Comment, ListingComment)