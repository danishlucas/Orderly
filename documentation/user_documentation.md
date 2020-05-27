# User documentation

## A high-level description
Orderly is a chore household chore management web application. Users can create a household and add people to it, then assign daily or weekly chores. Users can then change chores or mark then as complete which will show up in a household feed for the rest of the household.

## How to install the software

### Clone the front end and back end repositories
```bash
git clone git@github.com:sweekruthi/orderly-web.git

git clone git@github.com:danishlucas/Orderly.git
```

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

## How to run the software
1. Running Django server for backend: 
    ```bash
    cd Orderly/orderly
    python manage.py runserver
    ``` 

2. Running React server for front end: 
    ```bash
    npm start
    ```   

Navigate to the instructed IP address and you should be able to see our web app! 

## How to use the software

### Creating an account and Logging in

On the home page, enter your email ID and password in the provided fields. The password must be at least 5 characters long. Click on the "Create an account" button to create your account.

After creating an account, you can log in by entering your email ID and password. Clicking on the "Log in" button will take you to your households page.

### Managing your houshold (work in progress)

#### Creating a household

On the "My households" page, click on the "Add household" button on the left. You will be prompted to enter a name for your household. Use the "+" button under "Members" to enter the email IDs of your household members.

Click on the "Create household" button to create your household. You will taken to the household page where you can [add chores](#adding-a-new-chore). 

To delete a household, click on the "Delete household" button on the bottom right.

#### Household notifications

You can view the recent household activities in the "Notifications" page. These activities may include - completion of chores by household members, addition/deletion of a member, addtion/deletion of a chore, etc.

#### Modifying household members

To add or remove household members, go to the "My households" page and click on the relevant household on the left. To add more members, click on the "+" button and enter their email IDs. To remove a member, click on the member to be removed. You will see an option to remove the household member. Hit the "save" button to save changes and regenerate your chore schedule.

### Managing Chores (work in progress)

#### Viewing your chores

All of the chores for a user can be viewed on the chores page.  Chores a grouped into weeks.
All of the Chores for a specific week will be displayed at once. Either in a simple view. Which will simply list the title of 
the chore, or a detailed view, which will also allow the user to view supplies and a description for the chore. Views
can be switched by selecting the icons in the top right corner.  The type of chore being viewed(Upcoming, completed, overdue)
can be changed by selecting the buttons in the bottom left corner.

#### Adding a new chore

Chores can be added to a household under the households page by selecting a household.  Selecting the schedule button. 
And clicking the 'Add chore' button on the left.  When adding a chore a title must be provided.
Supplies and a description can also be added but they are optional.

#### Completing chores

To have a chore marked as complete the user must post a notification in their feed with a photo showing the completed chore.
Other users in the household can then click 'approve completion' on the notification.  Once enough users
have approved the notification the chore will be considered completed.

## Reporting a Bug

Please use GitHub issues on this repository to report any bugs. Go to the issues tab of this repository. Click on New Issue and write a report of the issue. Add the label 'bug' and submit the report.

Please make sure you followed all the setup instructions. Please also include the versions of the software you're using in the report.