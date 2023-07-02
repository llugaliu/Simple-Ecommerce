from django.urls import path

from . import views
app_name = 'item'
urlpatterns = [
    path('delete/<int:pk>/', views.delete,name='delete'),
    path('<int:pk>/', views.detail,name='detail'),
    path('<int:pk>/edit/', views.edit,name='edit'),
    path('new/', views.new,name='new'),
    path('', views.items,name='items'),
]