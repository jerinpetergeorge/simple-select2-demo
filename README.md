## simple-select2-demo

This is a minimal example which shows how to use the [**`django-simple-select2`**](https://github.com/jerinpetergeorge/django-simple-select2) package.

## How to
1. clone the repository
2. create a virtual environment, activate it and install the requirements
3. apply the migrations: **`python manage.py migrate`**
4. load seed data: **`python manage.py loaddata select2-seed-data.json`**
5. create a superuser to access Django admin: **`python manage.py createsuperuser`**
6. run the application: **`python manage.py runserver`**

There you are!!!

### Create Article by using Select2 widget
1. Django Admin: http://127.0.0.1:8000/admin/demo/article/
2. Django ModelForm: http://127.0.0.1:8000/demo/article/create/

