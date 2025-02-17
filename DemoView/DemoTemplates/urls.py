from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('page2/', views.page2),
    path('save/', views.save),
    path('edit/<int:id>/', views.edit),
    path('edit/<int:id>/update/', views.update),
    path('delete/<int:id>', views.delete),
    path('insert/', views.insert),
    path('insert/saveBook/', views.saveBook),
    path('insert/editBook/<int:id>/', views.editBook),
    path('insert/editBook/<int:id>/updateBook/', views.updateBook),
    path('insert/deleteBook/<int:id>/', views.deleteBook),
]