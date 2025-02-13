from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('page2/', views.page2),
    path('save/', views.save),
    path('edit/<int:id>/', views.edit),
    path('edit/<int:id>/update/', views.update),
    path('delete/<int:id>', views.delete),
]