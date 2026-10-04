
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.entry_page),
    path('home/',views.home),
    path('theme/',views.dark_theme),
    path('logout/',views.logout),
    path('register/',views.register),
    path('login/',views.login),
    path('update/',views.update),
    path('display/',views.display),
    path('send/',views.sending_email),
    path('store/',views.store),
    path('show/',views.show)
]
