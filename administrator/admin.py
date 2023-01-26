from django.contrib import admin
from administrator.models import Category,Product,Lead

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Lead)