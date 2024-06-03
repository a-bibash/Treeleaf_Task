from django.db import models

# Create your models here.

class ComputerBrands(models.Model):
    brand_name = models.CharField(max_length = 255)
    logo = models.URLField()

    def __str__(self):
        return self.brand_name
    

class ComputerSpecification(models.Model):
    generation = models.CharField(max_length = 255)
    price_min = models.FloatField()
    price_max = models.FloatField()
    ram = models.IntegerField()
    brand = models.ForeignKey(ComputerBrands, on_delete= models.SET_NULL, null=True)


    def __str__(self) -> str:
        return self.brand.brand_name
    
    

class Computer(models.Model):
    computer_code = models.CharField(max_length=20, unique=True)
    computer = models.ForeignKey(ComputerSpecification , on_delete= models.CASCADE)
    quantity = models.IntegerField()
    unit_rate = models.IntegerField()
    total_price= models.FloatField()


    def save(self,*args, **kwargs):
        self.total_price= self.quantity * self.unit_rate
        super().save(*args, **kwargs)

    
    def __str__(self) -> str:
        return self.computer_code