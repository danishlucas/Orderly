pip install virtualenv 
virtualenv -p python3 orderlyenv
source orderlyenv/Scripts/activate
pip install -r ./requirements.txt 

cd orderly

python manage.py runserver