from django import forms
from blog.models import Comment

# Comment form
class CommentForm(forms.ModelForm):
    """ Summary:
        - Gets model from models of blog. Then show it in
          the blog-detail template.
    """
    
    class Meta:
        model = Comment
        exclude = ["applied"]
