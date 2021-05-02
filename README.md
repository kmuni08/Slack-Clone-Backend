# Slack-Clone-Backend

pages directory:
  This is where our project code will go ranging from creating models, serializers, url paths specific to the project and the views (API endpoints). 
  

In the Slack-Clone-Backend directory, to run the project type
python3 manage.py runserver

You'll be taken to the root http://localhost:8000/ or http://127.0.0.1:8000/ which currently isn't directed to any webpage, just returns a JSON response "Hello World". This api endpoint is in /pages/views.py  

def home(request: HttpRequest):
    return JsonResponse({"msg": "Hello World"})

What needs to be done:

In the 
/pages/views.py 

exchange_code funcion I need to put the client_id, client_secret etc in a .env file so that it's hidden. I'll refactor tomorrow. 

The "MyTokenObtainPairSerializer" class (I saw it on udemy and its used to do JWT auth for form data. 
However for the form data, currently the post request is on django admin. (On the cloud locally). 
It is saving to django admin, 
if you want to create one the command is
python3 manage.py createsuperuser

To access django admin you must run
python3 manage.py runserver

and the url path should be 
http://127.0.0.1:8000/admin
Login with the credentials you put in the "createsuperuser" command. 

If you test the API endpoint for registerUser on postman (url for that endpoint is found in 
/pages/urls.py) it will work. 

This needs to be refactored as well, since we agreed to save it to the postgresql database. 

For Google Auth request to get token I installed python's pipenv:

pip install pipenv  

And then used pipenv to install requests
pipenv install requests 

In the views.py I did 
import requests

One more important thing:
In slackclonebackend/settings.py
scroll to "DATABASES" and put in your
password to your PostgreSQL db. I took mine out for now. 

I hope this was helpful. 
