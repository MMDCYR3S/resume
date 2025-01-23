from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Post model
class Post(models.Model):
    """ Summary:
        - Post model that has built with many fields:
            1- User use foreign key to recognize the user
               that has been created.
            2- Categories that use many-to-many field.
            3- tags that use django taggit.
            4- counted-likes and counted-views to show how many
               likes and views a post has.
            5- Status that gives you the condition of a post.
    """
    photographer = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="blog/", default="blog/default.jpg")
    title = models.CharField(max_length=250)
    content = models.TextField()
    categories = models.ManyToManyField("Category")
    tags = TaggableManager()
    status = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    counted_likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ["-created_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return self.title
    
# Category model
class Category(models.Model):
    """ Summary:
        - Just have a name.
        - Use many-to-many field to identify category.
    """
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
# Comment model
class Comment(models.Model):
    """ Summary:
        - This function gets a post from the Post model and
          then, it shows the comment in the relevant post.
    """
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    applied = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]
    
    def __str__(self):
        return self.name
    
