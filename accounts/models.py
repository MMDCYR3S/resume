from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from django.contrib.auth.models import(
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Custom user manager
class UserManagementSystem(BaseUserManager):
    """ Summary:
        - Custom user management model that control and manage
          users' permission and access.
    """
    
    # Create normal user
    def create_user(self, email, password, **extra_fields):
        """ Summary:
            - Create user with email and password.
        """
        if not email:
            raise ValueError(_("Your email must be set!"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    # Create superuser
    def create_superuser(self, email, password, **extra_fields):
        """ Summary:
            - Create superuser with email and password.
            - This function checks user permissions and if the user
              doesn't have required permissions, it shows error.
        """
        
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") != True:
            raise ValueError(_("Superuser must have staff permissions!"))
        
        if extra_fields.get("is_superuser") != True:
            raise ValueError(_("Superuser must have superuser permissions!"))
        
        return self.create_user(email, password, **extra_fields)

# User model
class User(AbstractBaseUser, PermissionsMixin):
    """ Summary:
        - Custom user model that gets email as username
    """
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManagementSystem()
    
    def __str__(self):
        return self.email
    
# Profile model
class Profile(models.Model):
    """ Summary:
        - Profile model that complete information of the user.
        - Gets email from User model and put it in the user
          variable below.
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="accounts/", default="blog/default.jpg")
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    job = models.CharField(max_length=250, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{11}$')
    phone = models.CharField(validators=[phone_regex] ,max_length=11, unique=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
    
# Save profile to user
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **extra):
    """ Summary:
        - Gets User model as sender. If the user updates,
          the function updates the profile and shows it.
          If it's not, then a new profile will be created.
    """
    if created:
        Profile.objects.create(user=instance)
    
    