from django.contrib import admin
from blog.models import Post, Category , Comment

# Blog admin panel
class PostAdminPanel(admin.ModelAdmin):
    list_display = (
        "title",
        "photographer",
        "status",
        "counted_views",
        "counted_likes",
        "created_date",
        "published_date",
    )
    list_filter = ("photographer", "status", "published_date")
    search_fields = ("title", "content")
    
# Comment admin panel
class CommentAdminPanel(admin.ModelAdmin):
    list_display = ("name", "post", "email", "applied", "created_date")    
    list_filter = ("email",)
    search_fields = ("email", "post")

admin.site.register(Post, PostAdminPanel)
admin.site.register(Category)
admin.site.register(Comment, CommentAdminPanel)
