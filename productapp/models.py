from django.db import models

# Create your models here.
class Categorycloth(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    def __str__(self):
        return self.name
    
class Productcloth(models.Model):
    category = models.ForeignKey(Categorycloth,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Sizecategory(models.Model):
    size=models.CharField(max_length=100)
    def __str__(self):
        return self.size

class ProductVariant(models.Model):
   product = models.ForeignKey(Productcloth,on_delete=models.CASCADE,null=True,blank=True)
   csize = models.ForeignKey(Sizecategory,on_delete=models.CASCADE,null=True,blank=True)
   actualprice=models.IntegerField()
   discountedprice = models.IntegerField()
   


