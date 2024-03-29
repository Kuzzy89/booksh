from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from booksh.accounts.forms import BookshUserCreationForm
from booksh.accounts.models import BookshUser, Profile


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/signin_user.html"
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = "accounts/signup_user.html"
    form_class = BookshUserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        # `form_valid` will call `save`
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


def signout_user(request):
    logout(request)
    return redirect('index')

