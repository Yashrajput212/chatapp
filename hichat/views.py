import os
import shutil
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms, template
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import *
import uuid




def my_random_string(string_length=5):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.



@login_required(login_url='/login')
def index(request):
    room = Room.objects.filter(users=request.user).order_by('-modified')
    chats = Message.objects.filter(room__in=room).order_by('-time')

    return render(request, "hichat/index.html", {
        "rooms": room,
        "chats": chats
    })


@csrf_exempt
@login_required(login_url='/login')
def contact(request):    
    contact_list = Contacts.objects.filter(user=request.user).values('id', 'name', 'owner__id', 'owner__username', 'owner__email', 'user__id', 'user__username', 'user__email').order_by('name')

    if request.method == "PUT":
        data = json.loads(request.body)

        name = data.get('name')
        email = data.get('email')

        try:
            owner = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({"error": "Invalid Email"}, status=404)


        if owner.email in [contact['owner__email'] for contact in contact_list] or name in [contact['name'] for contact in contact_list]:
            return JsonResponse({"message": "Already exist"}, status=302)
        else:
            try:
                new_contact = Contacts(name=name, owner=owner, user=request.user)
                new_contact.save()
                return JsonResponse({"message": "success"}, status=200)
            except IntegrityError:
                return JsonResponse({"message": "Already exist"}, status=302)
    else:
        return JsonResponse([contact for contact in list(contact_list)], safe=False)

@login_required(login_url='/login')
def search(request, q):
    contact_list = Contacts.objects.filter(user=request.user, name__icontains=q).values('id', 'name', 'owner__id', 'owner__username', 'owner__email', 'user__id', 'user__username', 'user__email').order_by('name')
    return JsonResponse([contact for contact in list(contact_list)], safe=False)

@csrf_exempt
@login_required(login_url='/login')
def sent(request, id):
    try:
        room = Room.objects.get(pk=id)
    except Room.DoesNotExist:
        return HttpResponse(status=400)
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get('text') is None:
            return JsonResponse({"error": "data empty"}, status=400)
        else:
            message = Message(text=data.get('text'), user=request.user, room=room)
            message.save()
            room.modified = datetime.datetime.now()
            room.last_modifier = request.user.id
            room.save()
            return JsonResponse({"message": "success"}, status=200)

@login_required(login_url='/login')
def room(request, name):
    try:
        room = Room.objects.get(name=name)
    except Room.DoesNotExist:
        return JsonResponse({"error": "room load error"})
    
    messages = list(Message.objects.filter(room=room).values('id', 'room', 'user', 'text', 'time').order_by('time'))

    return JsonResponse([message for message in messages], safe=False)

@login_required(login_url='/login')
def create_room(request, id):
    user2 = User.objects.get(pk=id)
    rooms = Room.objects.filter(users=request.user)
    for room in rooms:
        if user2 in room.users.all():
            print(room)
            return JsonResponse({"error": "room already exist", "room_id": room.id}, status=302)

    if request.method == "PUT":
        data = json.loads(request.body)

        message = data.get('text')

        name = my_random_string() + request.user.username + "~" + user2.username
        new_room = Room(name=name, modified=datetime.datetime.now())
        new_room.save()
        new_room.users.add(User.objects.get(pk=id), request.user)

        new_message = Message(text=message, user=request.user, room=new_room)
        new_message.save()
        new_room.modified = datetime.datetime.now()
        new_room.last_modifier = request.user.id
        new_room.save()
        return JsonResponse({"message": "room created", "room_id": new_room.id}, status=200)
    else:
        return JsonResponse({"error": "method must be a PUT"}, status=404)


@login_required(login_url='/login')
def load_rooms(request):
    rooms = Room.objects.filter(users=request.user).order_by('-modified')

    return JsonResponse([room.serialize() for room in rooms], safe=False)


@login_required(login_url='/login')
def all_messages(request):
    rooms = Room.objects.filter(users=request.user)
    messages = list(Message.objects.filter(room__in=rooms).values('id', 'room', 'room__name', 'room__last_modifier', 'room__read', 'user', 'text', 'time').order_by('-time'))

    return JsonResponse([message for message in messages], safe=False)


@csrf_exempt
@login_required(login_url='/login')
def read(request, id):
    try:
        room = Room.objects.get(pk=id)
    except Room.DoesNotExist:
        return JsonResponse({"error": "room does not exist"}, status=404)
    if request.method == "PUT":
        data = json.loads(request.body)

        if data.get('read') == "unread":
            room.read = False
            room.save()
            return JsonResponse({"message": "success"}, status=200)
        if data.get('read') == "read":
            room.read = True
            room.save()
            return JsonResponse({"message": "success"}, status=200)

    return JsonResponse({"error": "fail"}, status=400)



@login_required(login_url='/login')
def delete_chat(request, id):
    try:
        message = Message.objects.get(pk=id)
    except Message.DoesNotExist:
        return JsonResponse({"error": "message doese not exist!"}, status=404)

    message.delete()
    return JsonResponse({"message": "deleted"}, status=200)



@login_required(login_url='/login')
def delete_account(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        messages.success(request, "User does no exist")
        return HttpResponseRedirect('/login')
    AllRooms = Room.objects.filter(users=user)
    AllRooms.delete()
    user.delete()
    messages.success(request, 'Your account has been successfully deleted')
    return HttpResponseRedirect('/login')

@login_required(login_url='/login')
def change_password(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            messages.error(request, "User does no exist")
            return HttpResponseRedirect('/login')
        
        data = json.loads(request.body)
        if not data.get('Old_pass'):
            return JsonResponse({"error": "Please enter old password."})
        if not data.get('New_pass'):
            return JsonResponse({"error": "Please enter new password."})
        
        auth_user = authenticate(request, email=request.user.email, password=data.get('Old_pass'))

        if not auth_user:
            return JsonResponse({"error": "Invalid old password."})

        if data.get('Old_pass') == data.get('New_pass'):
            return JsonResponse({"error": "New password must be different."})
        
        user.set_password(data.get('New_pass'))
        user.save()
        messages.success(request, "Your password has been successfully updated. Please login again.")
        return JsonResponse({"message": "Password update successfully."})



@login_required(login_url='/login')
def delete_contact(request, id):
    try:
        contact = Contacts.objects.get(pk=id)
    except Contacts.DoesNotExist:
        return JsonResponse({"error": "Contact does not exist."}, status=404)

    contact.delete()
    return JsonResponse({"message": "Contact delete successfully."}, status=200)


@login_required(login_url='/login')
def delete_room(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return JsonResponse({"error": "Room does not exist."}, status=404)

    room.delete()
    return JsonResponse({"message": "Room delete successfully."}, status=200)



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid email and/or password.")
            return render(request, "hichat/login.html")
    else:
        return render(request, "hichat/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords must match.")
            return render(request, "hichat/register.html")

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            messages.error(request, "Username already taken.")
            return render(request, "hichat/register.html")
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hichat/register.html")