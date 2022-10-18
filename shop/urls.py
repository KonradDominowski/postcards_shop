from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='shop-home'),
    path('add/', views.AddNewPhoto.as_view(), name='create_photo'),
    path('add/confirm/<int:photo_id>', views.ConfirmPhoto.as_view(), name='confirm_photo'),
    path('add/delete/<int:photo_id>', views.DeletePhoto.as_view(), name='delete_photo')
]
