from django.urls import path

from booksh.accounts.views import SignUpUserView, SignInUserView

urlpatterns = [
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
]