from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_user_view, name='get_user_view'),
    path('register',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout',views.logout, name='logout')
]