from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage

from django.views.generic.base import RedirectView


urlpatterns=[
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/hichat/favicon.ico'))),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("contact", views.contact, name="contact"),
    path("search/<str:q>", views.search, name="search"),
    path("create_room/<int:id>", views.create_room, name="create_room"),
    path("room/<str:name>", views.room, name="room"),
    path("sent/<int:id>", views.sent, name="sent"),
    path("load_rooms", views.load_rooms, name="load_rooms"),
    path("all_messages", views.all_messages, name="all_messages"),
    path("read/<int:id>", views.read, name="read"),
    path("delete_chat/<int:id>", views.delete_chat, name="delete_chat"),
    path("delete_account", views.delete_account, name="delete_account"),
    path("change_password", views.change_password, name="change_password"),
    path("delete_contact/<int:id>", views.delete_contact, name="delete_contact"),
    path("delete_room/<int:room_id>", views.delete_room, name="delete_room")
]