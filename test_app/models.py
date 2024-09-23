from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    image = models.ImageField(upload_to='img/',blank=True,null=True)  
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    # email=models.EmailField()
    class Meta:
        db_table='login'
    