from django.urls import path
from website.views import *
# create app_name
app_name = "website"

urlpatterns = [
    path("", index_view, name="index"),
    path("about/", about_view, name="about"),
    path("contact/", contact_view, name="contact"),
    path("samples/", sample_view, name="samples"),
    path("search/", search_field, name="search"),
]