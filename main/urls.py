from django.urls import path
from . import views

urlpatterns = [
    path('',views.posting, name='posting'),
    path('<id>',views.view_post, name='post'),
]