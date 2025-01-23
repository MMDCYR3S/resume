from django import template
from blog.models import Post, Category ,Comment

register = template.Library()

# Show recent posts
@register.inclusion_tag("blog/blog-recent.html")
def recent_posts(arg=3):
    """ Summary:
        - In this function, posts will be filtered by status and then
          It will be shown by date they were published.
    """
    posts = Post.objects.filter(status=True).order_by("-published_date")[:arg]
    context = {"posts": posts}
    return context

# Show categories
@register.inclusion_tag("blog/blog-categories.html")
def post_cat():
    """ Summary:
        - This function will show the categories. It gets category's name
          and after that, put it in the dictionary and show it.
    """
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(categories=name).count()
    context = {"categories" : cat_dict}
    return context

# Show tags
@register.inclusion_tag("blog/blog-tags.html")
def post_tags():
    posts = Post.objects.filter(status=True)
    context = {"posts": posts}
    return context

# Show comments
@register.inclusion_tag("blog/blog-recent-comment.html")
def recent_comments(count=3):
    comments = Comment.objects.filter(applied=True).order_by("-created_date")[:count]
    context = {
        "comments" : comments,
    }
    return context