from django.urls import path

from .views import (UserLoginView, UserLogoutView, UserRegisterView,
                    VerifyUserView, home, UserUpdateView, CreateAdminView, AdminListView)

app_name = "account"
urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("verify/", VerifyUserView.as_view(), name="verify"),
    path("update/<int:user_id>/", UserUpdateView.as_view(), name="update"),
    path("admin_create/", CreateAdminView.as_view(), name="admin_create"),
    path('admin_list/', AdminListView.as_view(), name='admin_list'),
    path("", home, name="home"),
]
