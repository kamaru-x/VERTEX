from django.db import models

# Create your models here.

class Category(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(auto_now_add=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    Name = models.CharField(max_length=50)
    Reference = models.CharField(max_length=20)
    Products = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

#################################################################################

class Product(models.Model):
    # default
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(auto_now_add=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    Category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True)
    Name = models.CharField(max_length=50)
    Price = models.FloatField()
    Reference = models.CharField(max_length=20)

    def __str__(self):
        return self.Name