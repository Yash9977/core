from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class destination(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    img=models.ImageField(upload_to="upload")
    offer=models.BooleanField(null=False)
    def save(self, *args, **kwargs):
        now=datetime.now()
        self.img.name=now.strftime("%Y-%m-%d,%H-%M-%S") 
        super(destination,self).save( *args, **kwargs)
       
class Search(models.Model):
    City=models.CharField( max_length=50)
    Departure=models.DateTimeField()
    Arrival=models.DateTimeField()
    Budget=models.IntegerField()
 
class session(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    token=models.CharField(max_length=100,null=False)
    def create_token(username):
        return username + datetime.now().strftime("%Y-%m-%d,%H-%M-%S")
								