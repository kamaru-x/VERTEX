from django.urls import path
from administrator import views

urlpatterns = [
    path('add-category/',views.add_category,name='add-category'),
    path('list-category/',views.list_category,name='list-category'),
    path('view-category/<int:cid>/',views.view_category,name='view-category'),
    path('edit-category/<int:cid>/',views.edit_category,name='edit-category'),
    path('delete-category/<int:cid>/',views.delete_category,name='delete-category'),
    
    path('add-product/',views.add_product,name='add-product'),
    path('list-product/',views.list_products,name='list-product'),
    path('edit-product/<int:pid>/',views.edit_product,name='edit-product'),
    path('delete-product/<int:pid>/',views.delete_product,name='delete-product'),

    path('add-salesman/',views.add_salesman,name='add-salesman'),
    path('list-salesman/',views.list_salesman,name='list-salesman'),
    path('edit-salesman/<int:uid>/',views.edit_salesman,name='edit-salesman'),

    path('add-leads/',views.add_lead,name='add-lead'),
    path('list-add/',views.list_leads,name='list-lead'),
    path('edit-lead/<int:lid>/',views.edit_lead,name='edit-lead'),
    path('view-lead/<int:lid>',views.view_lead,name='view-lead'),
    path('opertunity-convertion/<int:lid>/',views.opertunity_convertion,name='convert-op'),

    path('previous-meeting-details/<int:mid>/',views.previous_meeting_details,name='p-meeting-d'),
]