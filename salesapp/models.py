from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.




class BikeBrand(models.Model):
    name = models.CharField(max_length = 200, unique = True)
    image = models.ImageField(upload_to="cat_images", default="default.jpeg", null = True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length =200, null =True)
    
    def __str__(self):
        return self.name

class State(models.Model):
    state = models.CharField(max_length =200)

    
    def __str__(self):
        return self.state

class Tags(models.Model):
    name = models.CharField(max_length = 200, unique =True)

    def __str__(self):
        return self.name



class Bike(models.Model):
    name = models.CharField(max_length = 200, null =True)
    description = models.TextField(max_length =500, null = True)
    image = models.ImageField(upload_to="images" , default='default.jpeg', null=True,blank=True)
    fuel_type_choices = (
        ("petrol", "petrol"),
        ("EV", "EV"),)
    category_choices = (
        ("gear less", "Gear less"),
        ("gear", "Gear"),
    )
    category = models.CharField(max_length = 200,choices = category_choices ,null = True)
    bike_ownership_count = models.PositiveIntegerField()
    fuelType_object = models.CharField(max_length = 200, choices = fuel_type_choices)  
    registrationyear_object = models.PositiveIntegerField()
    state_object = models.ForeignKey(State, on_delete = models.CASCADE, null =True)
    city_object = models.ForeignKey(City, on_delete = models.CASCADE, null = True) 
    enginepower_cc = models.PositiveIntegerField()
    kms_driven = models.CharField(max_length = 10,  null = True)
    brand_object = models.ForeignKey(BikeBrand, on_delete =models.CASCADE)
    sale_status = models.BooleanField(default = False)
    user_object = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "owner")
    created_date = models.DateTimeField(auto_now_add = True)
    price = models.CharField(max_length = 200, null = True)
    updated_date = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
    def __str__(self):
        return self.name


class WishList(models.Model):
    user_object = models.OneToOneField(User, on_delete =models.CASCADE, related_name = "saved")
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    @property
    def wish_items(self):
        return self.saveditem.all()
    @property
    def wish_items_count(self):
        return self.wish_items.count()




class WishListItems(models.Model): 
    bike_object = models.ForeignKey(Bike, on_delete  = models.CASCADE,)
    wishlist_object = models.ForeignKey(WishList, on_delete = models.CASCADE, related_name="saveditem")
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)
     

class Enquiry(models.Model):
    user_object = models.ForeignKey(User, on_delete = models.CASCADE)
    bike_object = models.ForeignKey(Bike, on_delete =models.CASCADE)
    is_read = models.BooleanField(default = False, null = True)
    reply = models.TextField(max_length = 200, null = True)
    is_replied= models.BooleanField(default = False, null = True)
    message = models.TextField(max_length = 3000000000)
    created_date = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.message
    
class Feedback(models.Model):
    user_object = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", null =True)
    feedback = models.TextField(max_length = 200, null=True)

    

def create_wishlist(sender, instance, created,**kwargs):
    if created:
        WishList.objects.create(user_object =instance)

post_save.connect(create_wishlist, sender=User)


