# What To Dad Site

A social media web-application with Django.

## Features :

+ Author (User)
    + Input Author Info
      + First Name 
      + Last Name 
      + ID

+ Admin
    + CRUD Operations

+ Fatherly Bonds 
    + Author Post Topic: ID, Title, Content
    + Topic Post has ID, Content, Created Date, Title
    + Topic has "Likes" functionality

+ Activities
    + Author Post Topic: ID, Title, Content
    + Topic Post has ID, Content, Created Date, Title
    + Topic has "Likes" functionality
    
+ Top "Liked" Fatherly Bonds Posting
 + List of Top "Liked" Fatherly Bond Postings

 + Top "Liked" Activities Posting
 + List of Top "Liked" Activities Postings

## Technological considerations

+ asgiref==3.6.0
+ Django==4.1.4
+ sqlparse==0.4.3
+ Python 3.7
+ Bootstrap 4

### Needed Django models and their attributes
+ Author Model
+ PostLikes Model
+ Post Model

### URIs
Completed URLS:

    urlpatterns = [path('', PostList.as_view(), name='home'),
    path('fatherlybonds/', ForumBoard.as_view(), name='forumboard'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    ]

### Needed Django views and templates
+ Completed Views:
    + PostList
    + PostDetail
    + ForumBoard

+ Completed Templates:
    + base.html
    + forum.html
    + index.html
    + post_detail.html
    + sidebar.html
    + autocomplete.css
    + base.css
    + changelists.css
    + dark_mode.css
    + fonts.css
    + forms.css
    + login.css
    + nav_sidebar.css
    + responsive_rtl.css
    + rtl.css
    + widgets.css
    
### Deployment
Deployment URL: 
    
## Testing
+ Manual Testing

## General Guidelines
What To Dad is a social media web app developed with Django 2.1 and Python 3.7. This web apps has functionalities of adding posts for activities and "Fatherly Bonds". Activities can be upcoming activities or any fun activity for kids. "Fatherly Bonds" are bonding posts where dads can share thoughts, ideas, advice or ask questions. It also lets you "like" existing posts. What To Dad is a place where dads can find what to do as dads from activities to "Is it normal when.." type posts. 

## Installation

```bash
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv) pip install -r requirements.txt
    (venv) cd whatToDad_site
    (venv) python manage.py makemigrations
    (venv) python manage.py migrate
    (venv) python manage.py runserver
```

## Add django-allauth config

https://django-allauth.readthedocs.io/en/latest/installation.html#post-installation

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```
