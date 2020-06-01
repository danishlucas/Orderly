# Developer documentation

## How to obtain the source code
1. Clone the front end and back end repositories
    ```bash
    git clone git@github.com:sweekruthi/orderly-web.git
    
    git clone git@github.com:danishlucas/Orderly.git
    ```

## The layout of your directory structure
### In the Orderly Backend repository
* `README.md`: documentation for getting the project up and running
* `status_reports/`: folder containing weekly status reports of team progress
* `orderly/`: folder containing app content for Django
  * `manage.py`: python file for running important Django commands
  * `choremanagement/`: folder containing files for chore management module
    * `views.py`: contains all source code for the endpoints for the chore management module
    * `urls.py`: contains urls to link to the endpoints created in views.py
    * `tests.py`: contains tests for the chore management module
    * `models.py`: contains models specifically defined for chore management module
    * `admin.py`: registers all models to the site
  * `chorescheduling/`: folder containing files for the chore scheduling module
    * `views.py`: contains all source code for the endpoints for the chore scheduling module
    * `urls.py`: contains urls to link to the endpoints created in views.py
    * `tests.py`: contains tests for the chore scheduling module
    * `models.py`: contains models specifically defined for chore scheduling module
    * `admin.py`: registers all models to the site
  * `feedstructuring/`: folder containing files for the feed structuring module
    * `views.py`: contains all source code for the endpoints for the feed structuring module
    * `urls.py`: contains urls to link to the endpoints created in views.py
    * `tests.py`: contains tests for the feed structuring module
    * `models.py`: contains models specifically defined for feed structuring module
    * `admin.py`: registers all models to the site
  * `orderly/`: overall settings for Django app
    * `settings.py`: contains settings for the Django app
    * `urls.py`: contains url settings for all modules

### In Orderly-web repository
* `README.md`: contains instructions for running the project
* `src/`: folder containing all source files for the frontend repo
* `App/`: folder containing all files important for basic app function
* `Chores/`: folder containing all files related to chores and chore management
* `Households/`: folder containing all files related to households and household management
* `Login/`: folder containing all files related to users logging in
* `Notifications/`: folder containing all files related to notifications for users
* `Tests/`: folder containing all files for testing the frontend code


## How to build the software

### Setting up Django server for backend instructions: 

1. Install python3.

2. Navigate into root folder and create new virtual environment. 
        
    ```bash
    cd Orderly
    pip install virtualenv 
    virtualenv -p python3 orderlyenv
    ```

3. Activate the virtual environment. 
    ```bash
    source orderlyenv/bin/activate
    ```
    The following command will deactivate the virtual environment if needed. 
    ```bash
    deactivate
    ```   

4. Install required packages. 
    ```bash
    pip install -r requirements.txt 
    ``` 

### Setting up Node server for frontend instructions: 

1. Navigate to `orderly-web` repo
    ```bash
    cd orderly-web
    ```

2. Install required packages.
    ```bash
    npm install
    ```   

## How to test the software

### Running back end tests
```
cd Orderly/orderly
python manage.py test
```

### Running front end tests
```
cd orderly-web
npm test
```

## How to add new tests

### Back end
Tests can be easily run using the Django test runner. The environment can be set up and dependencies installed using the build instructions in the above section. The tests can then be executed by running `python manage.py test` in the directory containing manage.py. To run individual tests, use the `python manage.py test <insert-app-name>` option.

Each Django app already has a script called `test.py`. Test functions can be easily added to this script. Any function beginning with the prefix `test_` will be run as a test function.

### Front end
#### work in progress?

## How to build a release of the software
In this case, the commands for building the software and building a release of the software are both the same. Therefore, you can follow the instructions that we listed above. 

However, we do feel like it would be wise to implement some sort of versioning scheme, as we believe that this will help us keep track of different builds. When we release our web app, we will declare it as V1.0. Any future revision should be declared as 1.0.X, with the 0 indicating which of our versions the code was branched off of and the X indicating which version of your code it is. 
