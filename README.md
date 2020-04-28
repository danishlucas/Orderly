# Orderly
UW CSE 403 team project 

1. Install python3 and then install virtualenv
2. Make new directory to hold project and then create new virtual environment
  - virtualenv -p python3 orderlyenv

1. Navigate into root folder. 
- cd Orderly/orderly

2. Install virtualenv, then create new virtual environment and set it to run with python3. 
- pip install virtualenv 
- virtualenv -p python3 orderlyenv

3. Activate virtual environment. 
- source orderlyenv/bin/activate

4. Install required packages. 
- pip install -r requirements.txt 

5. Navigate to appropriate directory and get web server running. 
- cd Orderly/orderly/orderly
- python manage.py runserver

WEB SERVER SHOULD NOW BE RUNNING AT http://127.0.0.1:8000/

Follow the tutorial to get acquanted with Django:
- https://docs.djangoproject.com/en/3.0/intro/tutorial01/
