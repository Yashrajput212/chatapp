# Final-Project - HI'CHAT

Web Programming with Python and JavaScript

The project video is: https://youtu.be/sU5Yjgag7kA



# Distinctiveness and Complexity

  This project is distinct from all previous projects. This project is mostly a front-end base web application.
  
  This is a real-time chat application that does not need to reload the page to get new messages.

  This project includes lots of javascript functions that continuously run in the background and wait for a new update in the database.

  When JavaScript detects a new change such as a new message or deleting a message in the database the page automatically updates without reloading or requesting a new URL or page.

  The `complexity` of this project is constantly updating the client-side data but only updating the particular div or block that needs to be updated instead of updating the entire page.

  This project is all device responsive like foldable mobiles, tabs, iPad, Microsoft surface, etc.

  Creating a linebreak responsive textarea was too complicated.

  Getting the separate room name with code for each room is complicated, so I created a new custom function to generate the separate code each time.



# Introduction

This website is a real-time chat app created with Django. On this website, users can chat with friends with real-time messaging without reloading the page.

Users can create a new account to start chatting with other HI'CHAT users.

This is the final project for CS50's Web Programming with Python and JavaScript.



## Files

In the `template` folder:-

 - `layout.html` is a base HTML file containing header and bootstrap libraries.
 - `login.html` extends from `layout.html` and contains `Login Form` and alert messages.
 - `register.html` also extends from `layout.html` and contains `Register Form` and alert messages.
 - And the main file called `index.html` also extends from `layout.html` and contains the main structure of the application with all javascript functions.

The `static/hichat` folder contains a stylesheet with separated CSS properties.

All models are written in the `hichat/models.py` file.

All URLs are written in the `hichat/urls.py` file.

All Back-end functions are written in the `hichat/views.py` file.



#### Features

01. Login Existing User
02. Register User
03. Home Page
04. Contacts List & Add Contact
05. Search Contact
06. Start Chat with New Contact
07. Delete Contact
08. Unread / Read Message
09. Send / Delete Chat
10. Setting View / Update Password / Delete User Account / Delete Room
11. Super User



## Login Existing User

When you start the `HI'CHAT` web application, you are automatically redirected to the `Login Page` by default.

You need to log in first to go to the home page, otherwise, you can not access the home page without login.

If you enter the wrong credential login page shows an error alert.

If you don't have an account don't worry, you can click on the `Register` button to go to the register page.


## Register Page

In the top-right corner of the page, click on the `Register` button.

Now you are on the `Register` page.

New users can get registered by filling out the fields.

All fields are required.

To register as a new user, a username and email should be unique.

If you enter the wrong credential, an error alert appears like a `Bootstrap` alert module.

After you successfully register you automatically redirect to the home page.


## Home Page

When you successfully log in or register then you enter `Home Page` and you can see blank `Room List` and blank chat div.

In the `Home Page,` you can see your username in the top-right corner. The username is a button.

When you press your username button, a toggle list contains the `Setting` and `Logout` buttons.

At the bottom of the `Room List` is a round contact button for contact actions.

If you have any chats then the list of your room should have room buttons.

When you click on the room button, the chat view will be filled with chats.


## Contacts List And Add New Contact

On the home page, you can click on the contact button at the bottom of the `Room List`, and after the pop-up appears then click on add contact icon on the top-left corner to add new contacts.

After the contact was successfully saved user got an alert message "Contact Saved!".

When you click ok on the alert then a contact list pop-up appears and you can see saved contact.

If any error in saving the contact the error message appears on the top of the save contact pop-up.


## Search Contact

In the contact list view, you see a search bar, In the search bar, you can search for contacts that you have.

You can see that you don't need to click on any search button, When you type in the search box contact list will automatically filter by the search query.


## Start Chat with New Contact

In the contact list view, when you click on any contact button, a textarea will open then you can type a message and click on the send button to start chatting with that user.

After you send a message, the Django view function creates a new room and adds your message to the room and javascript will redirect you to that room.


## Delete Contact

In the Contact list view, you can see that if you have any contact in the list, the contact button has a `Trash Icon`.

When you click on the Trash button, a confirmation pop-up appears at the top.

If you confirm, the contact will delete, and if have any chat with that contact notice on the room name changes if you save or delete the contact.


## Unread / Read Message

On the home page, if you have chat and if it is still unread, the room button color should be green.

If you have received a new message and you are not in that room, pay attention to the `Room List`, the unread room will appear at the top of the `Room List`.

When you click the unread green room button, the button should turn orange and the room class should be changed from unread to read.


## Send / Delete Chat 

On the home page, If you have any chats or you can start new then in the room view, on the right side of the home page or at the bottom in mobile mode, you can see textarea at the bottom of the room view.

You can type a message and click on the send button to send a chat.

When you send a message your message is added to the room without reloading the page.

Your chats align to right with the trash icon and timestamps.

You can click the trash icon to delete a particular message.

Other users' messages align to the left side of the room view with timestamps but you can't delete them.


## Setting View / Update Password / Delete Room / Delete User Account

In the nav bar, If you logged in and on the home page, you can see your name in the right corner of the nav bar.

Your name is a button to toggle the list, the list contains setting and logout buttons.

Click the logout button to successfully log out of your account.

Or click on the setting button to open the setting view.

In the setting view, you can do multiple things like:-

  - #### Update Password

    In the setting view, you can change your password.

    If you enter the wrong or the same as the old password in the new password field, the error message shows.

    After successfully updating your password you will automatically log out and need to log in again with a new password.


  - #### Delete Room

    In the setting view, you can see the `Edit Room` Button.

    Click on the edit room button to toggle a pop-up window, that contains all rooms that you have.

    Every room has a trash button for deleting a particular room.


  - #### Delete User Account

    The setting view has a `Delete Account button at the bottom of the setting view.

    When you click on the Delete Account button a confirmation pop-up and if you confirm your account and data related to your account will delete completely.



# Back End

## Super User

Superuser is a feature provided by Django. The super user can manipulate all data in the Backend Management Dashboard.

The superuser can also view all the details of all users.


## Random Room Name

In views.py, define a custom function called `my_random_string` that can help to create a random room name every time.

Every Room name also contains both usernames.


# Front End

## User Interface Friendly

Everything in the client-side page view is easy to use and understand the structure of the application.

Colorful layouts and scrollable lists.

Pop-up windows with close buttons.

Completely Every device is responsive.

Full page view in desktop mode and sliders and pop-ups uses in mobile mode for a clear and big and easy-to-use layout.


## How to run the application

First, you have to install requirements.txt.

```shell script
pip install -r requirements.txt
```

After installing requirements run the following commands to migrate the database.

```shell script
python manage.py makemigrations
python manage.py migrate
```

Then run the application.

```shell script
python manage.py runserver
```

# Finally

Thanks to all CS50 staff for making [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) great.

Especially, thanks to [Brain Yu](https://www.edx.org/bio/brian-yu)'s excellent lecture and his "great question", which motivate me to finish the course study.