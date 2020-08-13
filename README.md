<h1 id='summary'>Summary</h1>

-   [xxxxxxxxx](#xxxxxxx)
    -   [xxxxxxxxx](#xxxxxxx)
    -   [xxxxxxxxx](#xxxxxxx)
    -   [xxxxxxxxx](#xxxxxxx)

<h1 id='django'>Django</h1>

<h2 id='startingproject'>Starting New Project</h2>

<h3 id='creatingnewproject'>Creating New Project</h3>

[Go Back to Summary](#summary)

-   Create a new project using `django-admin startproject django_rest_api`
-   Then `cd` to the project's folder

<h3 id='startingapp'>Starting New APP</h3>

[Go Back to Summary](#summary)

```Bash
  python3 manage.py startapp main_app
```

<h4 id='folderfiles'>Folder and Files</h4>

-   Create the following folder and files

    ```Bash
      touch main_app/static/favicon.ico
    ```

    -   This will prevent some warnings like `"GET /favicon.ico HTTP/1.1" 404 1981`

<h3 id='createdb'>Create Database</h3>

[Go Back to Summary](#summary)

-   In this example we are going to use postgreSQL
-   on the terminal run
    ```Bash
      psql
      \l
      CREATE DATABASE django_rest_api_db;
    ```

<h3 id='configserver'>Config Server</h3>

[Go Back to Summary](#summary)

-   in `django_rest_api/settings.py`:

    -   Let's config the basic server
    -   First import `environ` to work with environment variables

        ```Python
          environ.Env()
          environ.Env.read_env()
          my_db = os.environ['DATABASE']
          SECRET_KEY = os.environ['SECRET_KEY']
        ```

    -   Then we have to add the `main_app` to the `INSTALLED_APPS` array
    -   Then we need to config the database engine and database name, in `DATABASES` array

    ```Python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': my_db,
          }
      }
    ```

    -   After the `STATIC_URL` we add the login and logout redirect

    ```Python
      LOGIN_REDIRECT_URL = '/'
      LOGOUT_REDIRECT_URL = '/'
    ```

    <h3 id='migrations'>Migrations</h3>

[Go Back to Summary](#summary)

-   Migrations are used to update a database's schema (structure) to match the code in the Models.
-   Migrations are used to evolve a database over time - as the requirements of the application change. However, they can be "destructive" (cause a loss of data), so be careful with migrations if you're working with an application in production.
-   Migrations in Django are just Python files that are created by running a command Django in Terminal.

<h4 id='makemigrations'>Make Migrations</h4>

-   The following command creates migration files for all models that have been added or changed since the last migration:
-   `python3 manage.py makemigrations`

-   The output in the terminal informs us that the following migration file was created: `main_app/migrations/0001_initial.py`
-   A migrations directory is created for an app the first time you run **makemigrations**.

<h4 id='migrate'>Migrate</h4>

-   Simply creating migration files does not update the database.
-   To synchronize the database's schema with the code in the migration files, we "migrate" using this command:

```Bash
  python3 manage.py migrate
```

<h3 id='startingserver'>Starting Server</h3>

[Go Back to Summary](#summary)

```Bash
  python3 manage.py runserver
```

<h3 id='createsudo'>Create Super User</h3>

[Go Back to Summary](#summary)

-   The super user (administrator) is basically the owner of the site. When you are logged in to this account, you can access the Admin app to add additional users and manipulate Model data.
-   Run this command in the terminal:

    ```Bash
      python manage.py createsuperuser
    ```

-   Django will want you to create a password that's at least 3 characters long and complex, however, you can bypass it by typing `y` at the warning prompt.
-   You will prompted to enter a username, email address, and a password. You are now creating a 'web master' for your site!
-   Now go to your webpage and head over to the /admin route to see an administration portal!
-   To change the password

    ```Bash
      python3 manage.py changepassword <user_name>
    ```

<h3 id='addingmodules'>Adding Modules To Admin Page</h3>

[Go Back to Summary](#summary)

-   We register our Models in the `main_app/admin.py` file:

    -   We first import the the model
    -   Then we register

    ```Python
      from django.contrib import admin
      # import your models here
      from .models import auth_user

      # Register your models here
      admin.site.register(auth_user)
    ```
