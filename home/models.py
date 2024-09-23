from django.db import models
# from django.template.defaultfilters import truncatechars 
# from django.utils.safestring import mark_safe

class Note(models.Model):
    userr = models.CharField(max_length=30)
    uemail = models.CharField(max_length=20)
    ucomment = models.TextField()
    
    def __str__(self):
        return self.title

class UploadImage(models.Model):
    okmail = models.CharField(max_length=20)
    addr = models.CharField(max_length=70)
    comment = models.CharField(max_length=70)
    num = models.CharField(max_length=12)
    image = models.ImageField(null=True,blank=False,upload_to="media")
    def __str__(self):
        return self.okmail

