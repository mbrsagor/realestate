# realestate
Django, React, Redux, Docker, Celery, Redis, and NGINX -  real estate web-app

#### Setup

##### Dependencies

- Python 3.8
- Celery 5.2.3
- postgres  12.5

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop 
on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

###### 1st open in your system terminal then follow the command line.

```bash
git clone https://github.com/mbrsagor/realestate.git
cd realestate
```

###### Then copy code from the ``env_example`` and create new file `.env` then pasts

-------------------------------------------
```bash
|--> .env-sample
|--> .env
```

Run the application in your local development server:

```bash
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations user
./manage.py migrate user
./manage.py migrate
./manage.py createsuperuser
./mangae.py runserver
```


