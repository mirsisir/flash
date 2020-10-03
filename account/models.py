from django.db import models
from django.contrib.auth.models import User
from .utils import unique_order_id_generator
from django.db.models.signals import pre_save
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=100,null=True)

    email = models.CharField(max_length=100,null=True)
    def __str__(self):
	    return self.name

class ExtendedUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=100,blank=True, null=True, default=" " )
    phone = models.CharField(max_length=50,blank=True, null=True ,default="0")
    shop_name = models.CharField(max_length=100,blank=True, null=True, default=" ")
    pickup_address= models.CharField(max_length=400, blank=True, null=True, default=" ")
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
	#     return self.shop_name

class Order(models.Model):

    STATUS = (
        ('Return', 'Return'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('new order', 'new order'),
        ('hold', 'hold'),

        )
    order_id= models.CharField(max_length=120, blank= True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True , choices=STATUS, default='new order',blank=True)
    note = models.CharField(max_length=1000, null=True,blank=True)
    receiver_name= models.CharField(max_length=100)
    receiver_address= models.CharField(max_length=200)
    receiver_phone = models.CharField(max_length=50)
    order_number = models.CharField(max_length=50)
    condition= models.IntegerField(blank=True,default=0,null=True)
    order_date1 = models.DateField(auto_now_add=True,null=True)
    delivery_cost = models.IntegerField(default=60,null=True,blank=True)


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id= unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)

class payment(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    payment = models.IntegerField(default=0)
    
