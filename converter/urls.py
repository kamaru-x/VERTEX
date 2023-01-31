from django.urls import path
from converter import views

urlpatterns = [
    path('opportunities',views.list_opertunities,name='list-opportunities'),
    path('opportunity-view/<int:lid>',views.view_opertunity,name='view-opportunity'),

    path('proposal/<int:lid>/',views.create_proposal,name='proposal'),

    path('create-task/',views.create_task,name='create-task'),
    path('pending-task/',views.pending_task,name='pending-task'),
    path('completed-task/',views.completed_task,name='completed-task'),
    path('edit-task/<int:tid>/',views.edit_task,name='edit-task'),

    path('clients/',views.client_list,name='clients'),
    path('client-view/<int:cid>/',views.client_view,name='client-view'),

    path('accept/<int:lid>/',views.accept,name='accept'),

    path('projects/',views.projects,name='projects'),
    path('projects/<int:pid>/',views.view_project,name='view-project')
]