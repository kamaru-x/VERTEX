from django.db import models
from u_auth.models import User

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

#################################################################################

class Lead(models.Model):
    Date = models.DateTimeField(null=True)
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True)

    Edited_Date = models.DateTimeField(auto_now_add=True)
    EditedBy = models.IntegerField(default=0)
    EditedIp = models.GenericIPAddressField(null=True)

    Reference = models.CharField(max_length=20)
    Company = models.CharField(max_length=50)
    Address = models.CharField(max_length=250)
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    ECDate = models.DateField(null=True,blank=True)
    ESValue = models.FloatField()
    State = models.IntegerField()
    CName = models.CharField(max_length=50)
    CNumber = models.CharField(max_length=15)
    CMail = models.EmailField()
    Salesman = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Lead_Status = models.IntegerField(default=0)

    def __str__(self):
        return self.Company

#################################################################################

class Lead_Update(models.Model):
    Date = models.DateTimeField()
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True,blank=True)

    AddedDate = models.DateField(null=True)
    Lead = models.ForeignKey(Lead,on_delete=models.SET_NULL,null=True)
    Description = models.TextField()

    def __str__(self):
        return self.Lead.Company

#################################################################################

class Attachments(models.Model):
    Lead_Update = models.ForeignKey(Lead_Update,on_delete=models.SET_NULL,null=True)
    Attachment = models.FileField(upload_to='update-files')
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

#################################################################################

class Lead_Schedule(models.Model):
    Date = models.DateTimeField()
    Status = models.IntegerField(default=1)
    AddedBy = models.IntegerField(default=0)
    Ip = models.GenericIPAddressField(null=True,blank=True)


    AddedDate = models.DateField(null=True)
    Lead = models.ForeignKey(Lead,on_delete=models.SET_NULL,null=True)
    Mode = models.CharField(max_length=25)
    From = models.TimeField()
    To = models.TimeField()
    Description = models.TextField()

    def __str__(self):
        return self.Lead.Company