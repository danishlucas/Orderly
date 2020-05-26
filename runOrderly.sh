pip install virtualenv 
virtualenv -p python3 orderlyenv
source orderlyenv/Scripts/activate
pip install -r ./requirements.txt 

cd orderly

py manage.py runserver