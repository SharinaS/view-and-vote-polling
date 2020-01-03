# View and Vote Polling
A basic poll application built with Django and Python to explore and learn Django.

The app is composed of two parts:
1. A public site that allows users to view polls and vote in them
2. An admin site that allows for adding, changing and deleting polls.

The project is built within a virtual environment.



## Day 1: Project Setup
* Set up a repo
* Added gitignore
* Created a virtual env
* Created a project called polling
* Verified Django project works by checking the development server online
* Created app called polls

## Day 2: First View and Prep for Database
* Made an index view and wired it into the URLconf. Verified it works with `python manage.py runserver`, and navigated, via the URL, to /polls/.
* After the fact, made a .env file - future note - do this initially for settings file stuff.
* Edited polling > settings.py with time zone and put secret key in .env file.


# Contributor
Sharina Stubbs

# Technology Used
* Python 3.8
* Django 3.0
* Git and GitHub
* Atom
* SQLite

# Many Thanks
To the Django Docs that provided a tutorial to learn from.

# Resources
* [Setting up the project, an app, and a view](https://docs.djangoproject.com/en/3.0/intro/tutorial01/).
* [Setting up the database, creating a model, and getting started with the admin site](docs.djangoproject.com/en/3.0/intro/tutorial02/).
* [PEP8 Documentation of Naming Conventions](python.org/dev/pep-0008/#naming-conventions)
* [How to Get and Set .env variables](https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5)
