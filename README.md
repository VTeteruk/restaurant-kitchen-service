# Restaurant kitchen service - FoodieTrap

Django project for managing restaurant's kitchen with cooks, dishes and dish types

## Check it out!

[Restaurant project deployed to Render](https://restaurant-kitchen-service-rlsl.onrender.com)

## Using

You can use this username and password to login:

Username: `user`; Password: `user12345`

You can also create new user using the site (`I'm a chef button` in the navigation bar or `Add chief` near the list with all cooks)!

## Installation

Python3 must be already installed

```shell
git clone https://github.com/VTeteruk/restaurant-kitchen-service
cd restaurant-kitchen-service
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt
python manage.py runserver # starts Django Server
```

## Configuration

### Environment Variables

The project uses environment variables for configuration.
To set up the .env file, inside .env.sample file replace the placeholder values with your own. Then, rename it to .env.

## Features

* Authentication functionality for Cook/User
* Managing dishes, cooks & dish types directly from website interface
* Powerful admin panel for advanced managing
