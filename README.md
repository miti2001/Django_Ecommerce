# Django_Ecommerce
E-commerce websites are something that almost all users are well aware with. The following code tries to imitate such an E-commerce web Application with the help of Django. 

# Project Overview 
The web application covers some basic functionalities of an E-commerce website. It allows new users to sign-in to the webApp. Logged in users can view a list of products offered by the company. Users can add/ drop specified quantity of products to the cart and proceed to buy these items. The app will keep a record of the availability of the products and display the cart total to the users.  

# Running the project 
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
