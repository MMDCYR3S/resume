from django import forms
from website.models import ContactForm

# Contact Fields
class Contacts(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    subject=  forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)
    
# Contact Form
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactForm
        fields = "__all__"
