# Orderly

There are two parts to getting the application working: running the Django server for the backend, and running the Node server for the frontend.

Setting up Django server for backend instructions: 

1. Install python3.

2. Navigate into root folder and create new virtual environment. 
        
    ```
    cd Orderly
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
    pip install -r requirements.txt 
    ```   

5. Run tests
    ```
    cd Orderly/orderly
    python manage.py test
    ``` 

5. Navigate to appropriate directory and get web server running. 
    ```
    cd Orderly/orderly
    python manage.py runserver
    ```   

Setting up Node server for frontend instructions: 

1. Clone the following repo: https://github.com/sweekruthi/orderly-web 

2. Install required packages.
    ```
    npm install
    ```   

3. Launch the server.
    ```
    npm start
    ```   

Navigate to the instructed IP address and you should be able to see our web app! 

-----------------------------------------------------------------------------------------

Testing: 

In order to run our tests, you will need to navigate inside the orderly directory and run the tests from the manage.py file. Each of the following commands will run the tests for our individual modules:
    ```
    python manage.py test chorescheduling
    ```   
    ```
    python manage.py test choremanagement
    ```   
    ```
    python manage.py test feedstructuring
    ```   


