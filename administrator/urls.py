from django.urls import path
from administrator import views

urlpatterns = [
    path('add-category/',views.add_category,name='add-category'),
    path('list-category/',views.list_category,name='list-category'),
    path('delete-category/<int:cid>/',views.delete_category,name='delete-category'),
    path('add-product/',views.add_product,name='add-product'),
    path('list-product/',views.list_products,name='list-product'),
]