from django.contrib import admin
from administrator.models import Category,Product,Lead,Lead_Update,Lead_Schedule,Attachments,Proposal,Task

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Lead)
admin.site.register(Lead_Update)
admin.site.register(Lead_Schedule)
admin.site.register(Attachments)
admin.site.register(Proposal)
admin.site.register(Task)