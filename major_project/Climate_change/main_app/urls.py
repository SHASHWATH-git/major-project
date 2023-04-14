from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout,name='logout'),
    path('bookapi',views.bookapi,name='bookapi')
]