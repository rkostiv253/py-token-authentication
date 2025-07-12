from django.urls import path

from user.views import CreateUserView, LoginUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", LoginUserView.as_view(), name="get_token"),
    path("me/", ManageUserView.as_view(), name="manage_user"),
]

app_name = "user"
