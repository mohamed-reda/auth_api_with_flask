## Here is a brief description of the attributes that we will define in the recipe class:

• name: The name of the recipe.

• description: The description of the recipe.

• num_of_servings: The number of servings.

• cook_time: The cooking time required. This is an integer whose units are in seconds.

• directions: The directions.

• is_publish: The publish status of the recipe; the default is draft


------------------------------------------------------------------------------

Attached to this lecture as a Resource is a short guide on how to configure Flask-JWT—it includes things like:

Changing the authentication endpoint (by default, /auth);

Changing the token expiration time (by default, 5 minutes);

Changing the authentication key name (by default, username);

Changing the authentication response body (by default, only contains access_token); and

Changing the error handlers.

------------------------------------------------------------------------------
Authentication URL

app.config['JWT_AUTH_URL_RULE'] = '/login'

jwt = JWT(app, authenticate, identity)

------------------------------------------------------------------------------
Token Expiration Time

# config JWT to expire within half an hour

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

------------------------------------------------------------------------------
Authentication Key Name

# config JWT auth key name to be 'email' instead of default 'username'

app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

------------------------------------------------------------------------------
Authentication Response Handler


------------------------------------------------------------------------------

[comment]: <> (<img src="" width="800" height="400"  />  )



------------------------------------------------------------------------------

## commands

1

pip install -r requirements.txt

[comment]: <> ( Flask-2.1.3 )

------------------------------------------------------------------------------

check

django-admin --version

------------------------------------------------------------------------------

activate virtual environment:

pipenv shell

------------------------------------------------------------------------------

if this runs with no error:

2

django-admin startproject nandiasgarden .

so my virtual environment has Django installed properly.

here without (.) to the command, it will create config folder in config folder

------------------------------------------------------------------------------

3

django-admin startapp pizza

4

pip3 install django-widget-tweaks



------------------------------------------------------------------------------

running Django’s local web server

python manage.py runserver

exit

------------------------------------------------------------------------------

pipenv shell

exit


------------------------------------------------------------------------------

python manage.py startapp pages

• admin.py is a configuration file for the built-in Django Admin app

• apps.py is a configuration file for the app itself

• migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync

• models.py is where we define our database models which Django automatically translates into database tables

• tests.py is for our app-specific tests

• views.py is where we handle the request/response logic for our web app

------------------------------------------------------------------------------
Run:

python manage.py runserver

------------------------------------------------------------------------------
test:

python manage.py test

------------------------------------------------------------------------------

apply the migrations:

python manage.py migrate

change the user:

python manage.py createsuperuser

nilecrocodile

mohamed.reda.007007@gmail.com

12345678

------------------------------------------------------------------------------
after creating new model at notes, lets deal with the database:

python manage.py makemigrations

after showing the migration of which user who created the note, apply the default athe terminal as:

1

1

then apply the migrations:

python manage.py migrate

check:

python manage.py shell

from django.contrib.auth.models import User

user = User.objects.get(pk=1)

user

user.notes.count()

------------------------------------------------------------------------------
http POST localhost:5000/recipes name="Cheese Pizza" description="This is a lovely cheese pizza"

curl -i -X POST localhost:5000/recipes -H "Content-Type: application/ json" -d '{"name":"Cheese Pizza", "description":"
This is a lovely cheese pizza"}'
