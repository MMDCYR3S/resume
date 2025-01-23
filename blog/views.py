from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Count

from blog.models import Post , Category , Comment
from blog.forms import CommentForm

from django.contrib import messages

# Blog view
def blog_view(request, **fields):
    """ Summary:
        - A function for showing posts. Fields are the kwargs and
          used for getting extra fields(like category) and search
          the posts that contains these fields and show them to a
          user.
        - Use paginator to paginate posts.
    """
    # Posts - Categories, Total Posts Count
    posts = Post.objects.filter(status=True)
    categories = Category.objects.annotate(post_count=Count("post"))
    total_post_count = posts.count()
    
    if fields.get("cat_name") != None:
        posts = Post.objects.filter(categories__name = fields["cat_name"])
        
    if fields.get("author_user") != None:
        posts = Post.objects.filter(photographer__username = fields["author_user"])
        
    if fields.get("tag_name") != None:
        posts = Post.objects.filter(tags__name__in = [fields["tag_name"]])
    
    # Pagination
    posts = Paginator(posts, 9)
    try:
        page_num = request.GET.get('page')
        posts = posts.get_page(page_num)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    
    context = {
        "posts": posts,
        "categories": categories,
        "total_posts": total_post_count,
    }
    
    return render(request, "blog/blog-home.html", context)

def detail_view(request, name):
    """ Summary:
        - This function is for showing every post in the
          relevant html file with post's title.
        - It's use for showing the comments of the
          relevant post in the bottom and get new comments.
    """
    
    # Check if the request method is right and the form is valid
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "دیدگاه شما ارسال شد و در انتظار تأیید است.")
        else:
            messages.error(request, "خطا در ارسال دیدگاه! لطفاً مجدداً تلاش کنید.")
            
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, title=name)
    
    comments = Comment.objects.filter(post=post.id ,applied=True)
    form = CommentForm()
    
    # Check if the user has already see the posts
    if not request.session.get(f"viewed_post_{post.id}", False):
        # Increment the view count 
        post.counted_views += 1
        post.save()

        # Mark the post as viewed by the user to not repeat again
        request.session[f"viewed_post_{post.id}"] = True
    
    context = {
        "post" : post,
        "comments" : comments,
        }
    
    return render(request, "blog/blog-detail.html", context)

# Search field for blog
def blog_search(request):
    posts = Post.objects.filter(status=True)
    if request.method == "GET":
        if s:= request.GET.get("s"):
            posts = posts.filter(content__contains=s)
    
    context = {"posts": posts}
    return render(request, "blog/blog-home.html", context)
