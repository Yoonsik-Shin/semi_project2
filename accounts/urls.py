from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete", views.detail_all, name="detail_all"),
    path("delete/", views.delete, name="user_delete"),
    path("update/", views.update, name="update"),
    path("profile/", views.profile, name="profile"),
    path("password/", views.change_password, name="change_password"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("charging/", views.charging, name="charging"),
]
