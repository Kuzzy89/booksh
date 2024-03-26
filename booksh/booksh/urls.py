
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("booksh.common.urls")),
    path("accounts/", include("booksh.accounts.urls")),
    path("books/", include("booksh.books.urls")),
    path("authors/", include("booksh.authors.urls")),

]
