from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Center(models.Model):
    name = models.CharField(max_length=200)
    location =  models.CharField(max_length=200)
    img = ImageField(manual_crop='1280x720')
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def create_helpcenter(self):
        self.save()

    def delete_helpcenter(self):
        self.delete()

    @classmethod
    def find_helpcenter(cls, hood_id):
        return cls.objects.filter(id=hood_id)

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    bio = models.CharField(max_length=300, blank=True, null=True)
    pic = models.ImageField(upload_to='images/', default='default.jpg', blank = True)
    center = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.owner.username
    
    
class Cloth(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=300)
    contact = models.CharField(max_length=300, blank=True, null=True)
    hood = models.ForeignKey(Center, on_delete=models.SET_NULL, null=True, blank=True)
    image = ImageField(manual_crop='1280x720')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()
    

