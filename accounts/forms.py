from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from django.core.validators import RegexValidator

# Create user form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']  # Use email as username field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email']
        self.fields['password1']
        self.fields['password2']
        
    
# Update user profile
class ProfileUpdateForm(forms.ModelForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$')
    
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "job", "phone", "description", "image")
        
    phone = forms.CharField(validators=[phone_regex], max_length=11, required=False)