from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    Tiles_name = models.CharField(max_length= 50 )
    Tiles_size = models.CharField(max_length= 20 ) 
    Tiles_choice= (
        ('kitchen', 'kitchen'),
        ('bathroom',' bathroom'),
        ('room', 'room')
    )
    Tiles_type = models.CharField(max_length= 50,blank= True, choices= Tiles_choice) 
    Tiles_desc = models.CharField(max_length= 100) 
    Tiles_rate = models.IntegerField(default= 0) 
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.Tiles_name



class OrderTiles(models.Model):
    Person = models.ForeignKey(User, on_delete= models.CASCADE, null= True,related_name='ordertiles')
    Person_name = models.CharField(max_length= 50) 
    Person_mobile_number = models.CharField(max_length= 10) 
    Person_address = models.CharField(max_length= 100) 
    Order_Tiles_name = models.CharField(max_length= 50)
    Order_Tiles_size = models.CharField(max_length= 20) 
    Order_Tiles_type = models.CharField(max_length= 40) 
    Order_Tiles_rate = models.IntegerField(default= 0) 
    Order_Tiles_Quantity= models.CharField(max_length= 100)
    Order_image = models.ImageField(upload_to='shop/images')
    Order_Tiles_Time= models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.Order_Tiles_name