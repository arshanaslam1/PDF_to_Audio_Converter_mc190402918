
# Requirements 
Redis
Django 4.0.4
Python 3.10

# Step
1. Install redis
2. Make Virtual Environment
3. run these commands

    ```pip install -r requirements.txt```
    ```python manage.py migrate```
    ```python manage.py runserver```
    ```celery worker -A settings --loglevel=INFO --pool=solo```
    