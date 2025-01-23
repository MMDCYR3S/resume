from django.shortcuts import render
from django.contrib import messages

from blog.models import Post
from website.forms import ContactForm
from website.models import PhotoSample
from accounts.models import User , Profile

# IndexView for home page
def index_view(request):
    """ Summary:
        - Get posts to show every post that has been created lately.
        - Get photos from the PhotoSample model and show them in the
          index page.(has limitation by 12)
        - Gets user email and after that, gets profile's user that equal
          to email in the User model and then show it in the index page.
    """
    photos = PhotoSample.objects.filter(status=True).order_by("-created_date")[:12]
    posts = Post.objects.filter(status=True).order_by("-published_date")[:3]
    user = User.objects.get(email="rezabahrami74@gmail.com")
    profile = Profile.objects.get(user=user)
    context = {
        "posts" : posts,
        "photos" : photos,
        "profile" : profile,
        }
    return render(request, "website/index.html", context)

# AboutView for about page
def about_view(request):
    user = User.objects.get(email="rezabahrami74@gmail.com")
    profile = Profile.objects.get(user=user)
    context = {"profile" : profile}
    return render(request, "website/about.html", context)

# ContactView for contact page
def contact_view(request):
    """ Description:
        - It gets request of the user. If it's POST, then it checks
          if the form is valid or not. If it is, it will save the
          form and the message.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = messages.success(request, "پیام شما به بنده ارسال شد!")
        else:
            message = messages.error(request, "متأسفانه پیام شما ارسال نشد! لطفاً تمامی موارد مهم را وارد کنید.")
    form = ContactForm()
    
    context = {"form": form}
    return render(request, "website/contact.html", context)

def sample_view(request):
    photos = PhotoSample.objects.filter(status=True)
    context = {"photos": photos}
    return render(request, "website/photo-samples.html", context)

def search_field(request):
    posts = Post.objects.filter(status=True)
    photos = PhotoSample.objects.filter(status=True)
    if request.method == "GET":
        if s:= request.GET.get("s"):
            posts = posts.filter(content__contains=s)[:3]
            photos = photos.filter(title__contains=s)[:12]
            
    context = {
        "posts": posts,
        "photos" : photos,
    }
    return render(request, "website/index.html", context)
