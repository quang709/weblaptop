from django.db import models

# Create your models here.
class Category(models.Model):
   categoryname = models.CharField(max_length=40)
   def __str__(self):
       s= str(self.categoryname)
       return s
class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    ram  = models.CharField(max_length=40)
    chip = models.CharField(max_length=40)
    amount = models.IntegerField(max_length=500,null=True,default=0)
    image = models.ImageField(null=True)

    categoryname = models.ForeignKey(Category, on_delete=models.CASCADE)



    def __str__(self):
        s = "name:" + str(self.name) + " price:" + str(self.price)+" ram:" + str(self.ram)+" chip:" + str(self.chip)+" amount:" + str(self.amount) +" image:" + str(self.image)+"category:" + str(self.categoryname)
        return s
