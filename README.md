# AMA Saunas

![alt text](/assets/docs/wireframes/shop-final-img.PNG "Image of the website appearance on different screen sizes")  

Fully published website is here: [AMA Saunas](https://saunas-shop-22fabe13bf89.herokuapp.com/)

## Table of Contents
- [About](#about)
    - [Site purpose](#site-purpose)
    - [Target audience](#target-audience)
    - [Goals](#goals)
- [Structure](#structure)
    - [Website Pages](#website-pages)
    - [Code Structure](#code-structure)
    - [Database](#database)
    - [User Stories](#user-stories)
- [Design](#design)
    - [Wireframes](#wireframes)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Images](#images)
- [Features](#features)
    - [Website Features](#website-features)
    - [Future Implementations](#future-implementations)
- [Technologies Used](#technologies-used)
    - [Main Languages Used](#languages)
    - [Frameworks, Libraries & Programs Used](#frameworks)
- [Testing](#testing)
    - [Automated Tests](#automated-tests)
    - [Validation](#validation)
- [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku](#heroku)
- [Credits](#credits)


## About <a name="about"></a>

AMA Saunas is a small business lead by a craftsman, who provides various sizes of barrel saunas, and make them by customer needs.

### Site Purpose <a name="site-purpose"></a>
- The site purpose is to have users to learn about new small business and purchase their items.

### Target Audience <a name="target-audience"></a>
- This site is developed for anyone who is passionate about healthy lifestyle. 
- This site is developed for anyone who would wish to purchase a fully customizable barrel sauna. 
- This site is developed with thaught that it easy accessable to all users. Compatibility with different device sizes makes the contect easy accessible and readable on desktop or the mobile device.


### Goals <a name="goals"></a>
- This is a small step towards promoting a small business to the world and gaining new customers.
- To offer a user-friendly platform.
- To produce code that complies with best practices.


## Structure <a name="structure"></a>
### Website Pages <a name="website-pages"></a>
Website pages described below

| Page | Description |
| --- | --- |
| Home | Home page displays a hero image and the button to the all product page. At the bottom, there is also newsletter signup field and link to facebook page. |
| All Products | Display all available products in the shop. |
| Categories | Currently there are two categories for products in nav ba dropdown to be selected from. |
| Selected Items page | Product overview page, where details of the selected product are displayed. You can select buttons back to the product list or add item to the basket. |
| Cart page | This page will display all the items that are added to cart. Also, user can edit how many items they wish to purchase, or delete the item. |
| Checkout page | The provides ability to fill out the form to purchas the item. |
| Profile | On user profile page, the user can update information about themselves. |
| Login | The website user can login to their account. |
| Logout | The website user can logout of their account. |
| Register | The website user can register a new account. |
| Admin Login | The admin of the website can log into the store backend and edit the items or delete them. |


### Code Structure <a name="code-structure"></a>
- The project contains several apps. 
- The projects apps handles all data accordingly.
- The project also have files: 
    - templates
    - README.md
    - Procfile
    - requirements.txt
- The project was built on basis of a BoutiqueAdo walkthrough project from Code Institute.



## Deployment  <a name="deployment"></a>

Before getting to the deployment part, make sure you have set up accounts in [ElephantSQL](https://www.elephantsql.com/) and also [Cloudinary](https://cloudinary.com/).
You will keys provided by these two application to connect to the project and include them into your env.py file. 

### Local Deployment <a name="local-deployment"></a>

You can clone this repository and run it locally with the following steps:

- Login to GitHub (https://wwww.github.com)
- Select the repository [Passport Pages](https://github.com/AiGaA/passport-pages)
- Click the Code button and copy the HTTPS url, for example: https://github.com/AiGaA/passport-pages.git
- In your IDE, open a terminal and run the git clone command, for example: git clone https://github.com/AiGaA/passport-pages.git
- The repository will now be cloned in your workspace
- You will need to create your own env.py file and this should be added to .gitignore file too (so this is not commited and exposed to public) 
- In env.py add the following code with the relevant key, value pairs, and ensure you enter the correct key values

```
import os
os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'
os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'
os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'
```

- Install the relevant packages as per the requirements.txt file
- In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
- Ensure debug is set to true in the settings.py file for local development
- Run "python3 manage.py makemigrations" to check the status of the migrations
- Run "python3 manage.py migrate" to migrate the database
- Run "python3 manage.py createsuperuser" to create a super/admin user
- Start the application by running python3 manage.py runserver and it will open a new window. 
- This will prompt with an error, and you will need to copy the url provided to your ALLOWED_HOSTS
- Run the project once more


### Heroku <a name="heroku"></a>

This project can be deployed to Heroku with the following steps:

- Ensure debug is set to false in the settings.py file
- Run "python3 manage.py makemigrations" to check the status of the migrations
- Run "python3 manage.py migrate" to migrate the database
- Run "python3 manage.py createsuperuser" to create a super/admin user
- Create an account on [Heroku](https://www.heroku.com/)
- Create an app, give it a name, and select a region
- Under resources search for postgres, and add a Postgres database to the app
- Note the DATABASE_URL, this needs to be set as an environment variable in Heroku and your local environment variables
- Create a Procfile with the text: web: gunicorn passportpages.wsgi
- Make sure you add your environment variables (env.py) to Heroku's Config Vars
- In the settings.py ensure the connection is to the Heroku postgres database
- Ensure debug is set to false in the settings.py file
- Add 'localhost', and 'passportpages.herokuapp.com' to the ALLOWED_HOSTS variable in settings.py
- Connect the app to GitHub, and enable automatic deploys from main
- Click deploy to deploy your application to Heroku for the first time

## Credits  <a name="credits"></a>

I wish to say big thank you for everyone at Code Institute (CI) and Slack community for great help on this project when stuck the most. 
The project was based on CI walkthrough project 'Boutique Ado'.
