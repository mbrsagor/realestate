# leadmanager
> Lead manager backend API app.

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the Django apps on Windows, you should have little problem getting up and running.

### Run the application in your local dev server.

###### Prerequisites
- Python3.8
- psql (PostgreSQL) 13.2
- Al least know Django & Django DRF 
- Database concept

Copy the ``.env-sample`` rename ``.env`` otherwise you can't run the server.

> Open your terminal then, Please following the instructions for running the application in your local server.

```base
git clone https://github.com/mbrsagor/leadmanager.git
cd leadmanager
virtualenv venv --python=python3.8
source venv/bin/activate
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

N:B: After clone you have to change database configuration from config folder then `db.config.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'leadmanager',
        'USER': 'mbr-sagor',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

##### If you want to run the project ``docker`` pls follow the instructions:
```bash
docker-compose up
```
