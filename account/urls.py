from django.urls import path

from .views import UserLoginView, UserLogoutView, UserRegisterView, VerifyUserView

app_name = "account"
urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("verify/", VerifyUserView.as_view(), name="verify"),
]
