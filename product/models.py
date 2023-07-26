from django.db import models
from owner.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


product_categories =(("Groccery","Groccery"),
                  ("Electronics","Electronics"),
                  ("Textile","Textile"),
                  ("Health","Health"),
                  ("Home_appliences","Home_appliences"),
                  ("Footwears","Footwears"),
                  ("Toy","Toy"),
                  ("Furniture","Furniture"),
                  ("other","other"),
                )
qauntity_unit = (("kg","kg"),
                 ("gm","gm"),
                 ("unit","unit"),
                 ("set","set")
                )

class NotInterested(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null =False, blank=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')


class Product(models.Model):
    name = models.CharField(max_length=200, null =False, blank=False)
    images = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.CharField(max_length=500,blank=True,null=False,)
    price = models.IntegerField()
    per_unit =models.CharField(max_length=10,choices= qauntity_unit,default="unit")
    quantity = models.CharField(max_length=10,blank=False)
    category= models.CharField(max_length=200,choices= product_categories)
    not_interested = GenericRelation(NotInterested,related_query_name='product')

    def __str__(self):
        return self.name

    def __str__(self):
        return  "{}".format(self.name)


class UserProduct(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.CASCADE, null =False, blank=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null =False, blank=False)
