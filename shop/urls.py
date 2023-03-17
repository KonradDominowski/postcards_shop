from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, views_api

urlpatterns = [
    path("", views.Home.as_view(), name="shop-home"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("add/", views.AddNewPhoto.as_view(), name="create_photo"),
    path(
        "add/confirm/<int:photo_id>", views.ConfirmPhoto.as_view(), name="confirm_photo"
    ),
    path("add/delete/<int:photo_id>", views.DeletePhoto.as_view(), name="delete_photo"),
    path("update/<pk>", views.UpdatePhoto.as_view(), name="update_photo"),
    path("search/", views.SearchPhoto.as_view(), name="search_photo"),
    path("api/", views_api.PhotoListView.as_view(), name="photo_api"),
    path("api/add/", views_api.CreatePhotoView.as_view(), name="add_photo_api"),
    path(
        "api/thumbnails", views_api.ThumbnailListView.as_view(), name="thumbnails_view"
    ),
]
