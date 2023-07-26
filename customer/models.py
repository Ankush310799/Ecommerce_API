from django.db import models
from owner.models import User
from product.models import Product

user_action =(("Buy","Buy"),
            ("Add To Cart","Add To Cart"),
            )

class CustomerProductView(models.Model):
    product = models.ForeignKey(Product,null=False,blank=False,on_delete=models.CASCADE)
    not_interested= models.BooleanField(default=False)
    is_created = models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.product)

class CustomerCart(models.Model):
    name = models.ForeignKey(User,null =False, blank=False,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=False,blank=False,on_delete=models.CASCADE)
    action = models.CharField(max_length=200,choices= user_action,blank=True)
    quantity = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def __str__(self):
        return "{}".format(self.product)

    def __str__(self):
        return "{}".format(self.action)
