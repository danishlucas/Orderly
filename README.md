# Orderly

1. Install python3.

2. Navigate into root folder and create new virtual environment. 
        
    ```
    cd Orderly/orderly
    pip install virtualenv 
    virtualenv -p python3 orderlyenv
    ```

3. Activate the virtual environment. 
    ```
    source orderlyenv/bin/activate
    ```
    The following command will deactivate the virtual environment if needed. 
     ```
    deactivate
    ```   

4. Install required packages. 
    ```
    pip install -r ../requirements.txt 
    ```   

5. Navigate to appropriate directory and get web server running. 
    ```
    cd Orderly/orderly/orderly
    python manage.py runserver
    ```   

WEB SERVER SHOULD NOW BE RUNNING AT http://127.0.0.1:8000/. Click CONTROL + C to shut down the server.

Follow the tutorial to get acquanted with Django. There are 7 parts:
- https://docs.djangoproject.com/en/3.0/intro/tutorial01/
