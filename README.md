# Slack-Clone-Backend 
  
In the Slack-Clone-Backend directory, to run the project type
python3 manage.py runserver

You'll be taken to the root http://localhost:8000/ or http://127.0.0.1:8000/ which currently isn't directed to any webpage, just returns a JSON response "Hello World". This api endpoint is in /pages/views.py  

def home(request: HttpRequest):
    return JsonResponse({"msg": "Hello World"}
    
If you want to create a django admin account (one way to insert data other than Postman) the command is
python3 manage.py createsuperuser

To access django admin you must run
python3 manage.py runserver

and the url path should be 
http://127.0.0.1:8000/admin
Login with the credentials you put in the "createsuperuser" command. 

If you test the API endpoint for register on postman (url for that endpoint is found in 
http://127.0.0.1:8000/authaccounts/register) it will work. 

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

TO CREATE A TABLE IN POSTGRESQL:
In Django, create a model in the model.py file. 
Once that is completed, run the following commands:
First command:
python3 manage.py makemigrations

You should see something on your terminal like:
Migrations for 'table'
../somepath/migrations/0001_initial.py
- Create model table

Second command:
python manage.py migrate

You should see something on your terminal like:
Operations to perform:
Apply all migrations: table

Running migrations:
Applying table.0001_initial... OK

And your table should be added to the database. 

To create a new folder in Django (like how I did for pages directory or authaccounts directory with all those files)... the command is 

python3 manage.py startapp <some name>
  


