from django.db import models

# Contact Form
class ContactForm(models.Model):
    """ Contact:
        - Gets required fields for contact to target person.
    """
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date",]
        verbose_name = "Contact"
        
    def __str__(self):
        return f"{self.name}"

# PhotoSample model
class PhotoSample(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="website/photo-samples")
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
