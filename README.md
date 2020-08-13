<h1 id='summary'>Summary</h1>

-   [Django](#django)
    -   [Starting New Project](#startingproject)
        -   [Creating New Project](#creatingnewproject)
        -   [Starting New APP](#startingapp)
            -   [Folder and Files](#folderfiles)
        -   [Create Local Database](#createdb)
        -   [Config Server](#configserver)
        -   [Migrations](#migrations)
            -   [Makemigrations](#makemigrations)
            -   [Migrate](#migrate)
        -   [Starting Server](#startingserver)
        -   [Create Super User](#createsu)
        -   [Models](#models)
            -   [Enabling Modules To Admin Page](#enablingmodules)
        -   [Serializers](#serializers)
            -   [Serializer](#serializer1)
            -   [ModelSerializer](#modelserializer)
        -   [URLS](#urls)
            -   [Project URLS](#projecturls)
            -   [App URLS](#appurls)
        -   [Views](#views)

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
      touch main_app/static/favicon.ico main_app/serializers.py + urls.py
    ```

    -   the `main_app/static/favicon.ico` will prevent some warnings like `"GET /favicon.ico HTTP/1.1" 404 1981`
    -   the `main_app/serializers.py` will convert the incoming data into django way to understand JSON, and transform the data into JSON when sending back data to the requester
    -   the `main_app/urls.py` will contain all the routes of our server (Function Base Views or Class Base Views)

<h3 id='createdb'>Create Local Database</h3>

[Go Back to Summary](#summary)

-   In this example we are going to use postgreSQL, on the terminal run:
-   For more information about PostgreSQL commands, check my other [README](https://github.com/Roger-Takeshita/Bootcamp-Software-Engineer/blob/master/W07D01_PostgreSQL.md)

    ```Bash
      psql
      \l
      CREATE DATABASE django_rest_api_db;
      \q
    ```

<h3 id='configserver'>Config Server</h3>

[Go Back to Summary](#summary)

-   in `django_rest_api/settings.py`:

    -   Let's config the basic server
    -   First import `environ` to work with environment variables

        ```Python
          import environ
          environ.Env()
          environ.Env.read_env()
          my_db = os.environ['DATABASE']
          SECRET_KEY = os.environ['SECRET_KEY']
        ```

    -   Then we have to add the `main_app` and `rest_framework` to the `INSTALLED_APPS` list

        ```Python
          INSTALLED_APPS = [
              'main_app',
              'rest_framework',
              'django.contrib.admin',
              'django.contrib.auth',
              'django.contrib.contenttypes',
              'django.contrib.sessions',
              'django.contrib.messages',
              'django.contrib.staticfiles',
          ]
        ```

    -   Then we need to config the default database engine and database name, in `DATABASES` list

        ```Python
          DATABASES = {
              'default': {
                  'ENGINE': 'django.db.backends.postgresql',
                  'NAME': 'django_rest_api_db',
              }
          }
        ```

    -   If we are serving `hmtl` to the user, after the `STATIC_URL` we add the login and logout redirect

        ```Python
          LOGIN_REDIRECT_URL = '/'
          LOGOUT_REDIRECT_URL = '/'
        ```

<h3 id='migrations'>Migrations</h3>

[Go Back to Summary](#summary)

-   Migrations are used to update a database's schema (structure) to match the code in the Models.
-   Migrations are used to evolve a database over time - as the requirements of the application change. However, they can be "destructive" (cause a loss of data), so be careful with migrations if you're working with an application in production.
-   Migrations in Django are just Python files that are created by running a command Django in Terminal.

<h4 id='makemigrations'>Makemigrations</h4>

-   The following command creates migration files for all models that have been added or changed since the last migration:

    ```Bash
      python3 manage.py makemigrations
    ```

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

<h3 id='createsu'>Create Super User</h3>

[Go Back to Summary](#summary)

-   The super user (administrator) is basically the owner of the site. When you are logged in to this account, you can access the Admin app to add additional users and manipulate Model data.

    ```Bash
      python manage.py createsuperuser
    ```

-   Django will want you to create a password that's at least 3 characters long and complex, however, you can bypass it by typing `y` at the warning prompt.
-   You will prompted to enter a username, email address, and a password. You are now creating a 'web master' for your site!
-   Now go to your webpage and head over to the `http://127.0.0.1:8000/admin` route to see an administration portal!
-   **To change the password**

    ```Bash
      python3 manage.py changepassword <user_name>
    ```

<h3 id='models'>Models</h3>

[Go Back to Summary](#summary)

-   in `main_app/models.py`
-   Every time we change our models, don't forget to **makemigrations** and **migrate** to update the **database**

    ```Python
      from django.db import models

      class Article(models.Model):
          title = models.CharField(max_length=100)
          author = models.CharField(max_length=100)
          email = models.EmailField(max_length=100)
          date = models.DateTimeField(auto_now_add=True)

          def __str__(self):
              return self.title
    ```

<h4 id='enablingmodules'>Enabling Modules To Admin Page</h4>

[Go Back to Summary](#summary)

-   We register our Models in the `main_app/admin.py` file:

    -   We first import the the model
        -   in this case we are importing all models (`*`)
    -   Then we register the model, so we can see on the administration panel

    ```Python
      from django.contrib import admin
      from .models import *

      admin.site.register(Article)
    ```

<h3 id='serializers'>Serializers</h3>

[Go Back to Summary](#summary)

-   The first thing we need to get started on our Web API is to provide a way of serializing and deserializing the app instances into representations such as `JSON`. We can do this by declaring serializers that work very similar to Django's forms. Create a file in the `main_app` directory named serializers.py and add the following.

<h4 id='serializer1'>Serializer</h4>

-   in `main_app/serializers.py`

    -   If we are using `serializers.Serializer` we copy the structure of our model and change the name **models** to **serializer**
        -   The first part of the serializer class defines the fields that get serialized/deserialized. The `create()` and `update()` methods define how fully fledged instances are created or modified when calling `serializer.save()`
        -   A serializer class is very similar to a Django Form class, and includes similar validation flags on the various fields, such as required, max_length and default.
        -   The field flags can also control how the serializer should be displayed in certain circumstances, such as when rendering to HTML. The `{'base_template': 'textarea.html'}` flag above is equivalent to using `widget=widgets.Textarea` on a Django **Form class**. This is particularly useful for controlling how the browsable API should be displayed, as we'll see later in the tutorial.

    ```Python
      from rest_framework import serializers
      from .models import *

      class ArticleSerializer(serializers.Serializer):
          title = serializers.CharField(max_length=100)
          author = serializers.CharField(max_length=100)
          email = serializers.EmailField(max_length=100)
          date = serializers.DateTimeField()

      def create(self, validated_data):
          return Article.objects.create(validated_data)

      def update(self, instance, validated_data):
          instance.title = validated_data.get('title', instance.title)
          instance.author = validated_data.get('author', instance.author)
          instance.email = validated_data.get('email', instance.email)
          instance.date = validated_data.get('date', instance.date)
          instance.save()
          return instance
    ```

<h4 id='modelserializer'>ModelSerializer</h4>

-   in `main_app/serializers.py` - It's important to remember that **ModelSerializer classes** don't do anything particularly magical, **they are simply a shortcut for creating serializer classes**:

    -   An automatically determined set of fields.
    -   Simple default implementations for the create() and update() methods.

    ```Python
      from rest_framework import serializers
      from .models import *

      class ArticleSerializer(serializers.ModelSerializer):
          class Meta:
              model = Article
              # fields = ['id', 'title', 'author']
              fields = '__all__'
    ```

    -   Using **shell** to add some data to work with

    ```Bash
      python manage.py shell

      # from article.models import Article
      # from article.serializers import ArticleSerializer
      from .models import Article
      from .serializers import ArticleSerializer
      from rest_framework.renderes import JSONRenderer
      from rest_framework.parsers import JSONParser

      article = Article(title="First Article", author="Roger", email="roger@email.com")
      article.save()

      article = Article(title="Second Article", author="Thaisa", email="thaisa@email.com")
      article.save()
    ```

    -

<h3 id='urls'>URLS</h3>

<h4 id='projecturls'>Project URLS</h4>

-   in `django_rest_api/urls.py`

    -   In Django, routes are defined within **URLconf** modules named **urls.py**.
    -   It's a best practice for each app to define its own and include those URLs in the **project URLconf**.
    -   We need to import `include` from `django.urls` so we can import the all of app `urls` (since we created one file `main_app/urls.py`)
    -   In there, we are going to define all the server endpoints
    -   To enable authentication `path('accounts/', include('django.contrib.auth.urls')),`
        -   [Django Authentication - Official Docs](https://docs.djangoproject.com/en/3.1/topics/auth/default/)

    ```Python
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('', include('main_app.urls')),
          path('admin/', admin.site.urls),
      ]
    ```

<h4 id='appurls'>App URLS</h4>

-   in `main_app/urls.py`

    -   we need to import `path`, `url` and `views`
    -   if we are using **Class Base Views** we need to define `.as_view()`
    -   The `name='article_list'` kwarg is optional but will come in handy for referencing the URL in other parts of the app, especially from within templates.

    ```Python
      from django.urls import path
      from django.conf.urls import url
      from . import views

      urlpatterns = [
          #! FUNCTION BASE VIEWS
          path('article/', views.article_list, name='article_list'),
          path('article/<int:article_id>/', views.article_detail, name='article_detail'),

          #! CLASS BASE VIEWS
          path('', views.IndexAPIView.as_view(), name='article_list_index_class'),
          path('articleclass/', views.ArticleAPIView.as_view(), name='article_list_class'),
          path('articleclass/<int:article_id>/', views.ArticleDetailsAPIView.as_view(), name='article_detail_class')
      ]
    ```

<h3 id='views'>Views</h3>

[Go Back to Summary](#summary)

-   in `main_app/views.py`

    -   The function `HttpResponse` is the simplest way to send something back in response to a request. It's like `res.send()` was in Express.
    -   The function `JsonResponse` is just like `res.json()`
    -   If we are rendering the templates to serve `html` to the user, we need to import **render**

        -   `from django.shortcuts import render`

    ```Python
      from django.http import HttpResponse

      def home(request):
        return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
    ```

    ```Python
      from django.http import HttpResponse, JsonResponse
      from .models import *      #+ Import all models
      from .serializers import * #+ Import all serializers

      from django.views.decorators.csrf import csrf_exempt

      from rest_framework.parsers import JSONParser
      from rest_framework.response import Response
      from rest_framework import status
      from rest_framework.decorators import api_view
      from rest_framework.views import APIView

      # = FUNCTION BASE VIEW
      @api_view(['GET', 'POST'])
      def article_list(request):
          if request.method == 'GET':
              articles = Article.objects.all()
              serializer = ArticleSerializer(articles, many = True)
              return Response(serializer.data)
          elif request.method == 'POST':
              serializer = ArticleSerializer(data=request.data)

              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
              else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      @api_view(['GET', 'PUT', 'DELETE'])
      def article_detail(request, article_id):
          try:
              article = Article.objects.get(pk=article_id)
          except Article.DoesNotExist:
              return HttpResponse(status=status.HTTP_404_NOT_FOUND)

          if request.method == 'GET':
              serializer = ArticleSerializer(article)
              return Response(serializer.data)
          elif request.method == 'PUT':
              serializer = ArticleSerializer(article, data=request.data)
              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          elif request.method == 'DELETE':
              article.delete()
              return Response(status=status.HTTP_204_NO_CONTENT)

      # = CLASS BASE VIEW
      class IndexAPIView(APIView):
          def get(self, request):
              articles = Article.objects.all()
              serializer = ArticleSerializer(articles, many=True)
              return Response(serializer.data)

      class ArticleAPIView(APIView):
          def get(self, request):
              articles = Article.objects.all()
              serializer = ArticleSerializer(articles, many=True)
              return Response(serializer.data)

          def post(self, request):
              serializer = ArticleSerializer(data=request.data)

              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      class ArticleDetailsAPIView(APIView):
          def get_object(self, article_id):
              try:
                  return Article.objects.get(id=article_id)
              except Article.DoesNotExist:
                  return HttpResponse(status=status.HTTP_404_NOT_FOUND)

          def get(self, request, article_id):
              article = self.get_object(article_id)
              serializer = ArticleSerializer(article)
              return Response(serializer.data)

          def put(self, request, article_id):
              article = self.get_object(article_id)
              serializer = ArticleSerializer(article, data=request.data)
              if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

          def delete(self, request, article_id):
              article = self.get_object(article_id)
              article.delete()
              return Response(status=status.HTTP_204_NO_CONTENT)
    ```
