from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('room-detail/<int:pk>', room_detail, name='room-detail'),
    path('profile/<int:pk>', profile, name='profile'),
    path('creat-room/', create_room, name="create-room"),
    path('update-room/<str:pk>', update_room, name='update-room'),
    path('delete-room/<str:pk>', delete_room, name='delete-room'),
    path('delete-msg/<str:pk>', delete_msg, name='delete-message'),
    path('create-cat/', category_room, name='create-cat'),
    path('category-up/<str:pk>', update_cat, name='category-up'),
    path('category-del/<str:pk>', delete_cat, name='category-del'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', registration, name='register'),
    path('catigories/',categories , name='cats'),
    path('recent-active/',recent_active , name='recent-active'),
    path('settings/<int:pk>',settings , name='settings'),
    path('active/<str:pk>',active , name='active'),
]
