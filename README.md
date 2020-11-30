# Django QR generator website
This project uploads a file and generates a qr-code with an URL to that file

## Environment

Tested on Django 3.1 and Python 3.8 but it should be compatible from 2.7.

## Installation

* If you, you can use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) to install
a compatible environment:

```
virtualenv env --python=python3
```

* Then, install packages

```
pip install -r requirements.txt
```

```
python manage.py migrate
```

## Project structure

This project structure was generated with [dree](https://www.npmjs.com/package/dree). 

```text
website_qr_generator
 ├── LICENSE
 ├── README.md
 ├── db.sqlite3
 ├── manage.py
 ├── requirements.txt
 ├─> web
 │   ├── __init__.py
 │   ├── admin.py
 │   ├── apps.py
 │   ├── forms.py
 │   ├─> migrations
 │   │   ├── __init__.py
 │   ├── models.py
 │   ├─> templates
 │   │   └─> web
 │   │       └── index.html
 │   ├── tests.py
 │   └── views.py
 └─> website_qr_generator
     ├── asgi.py
     ├── settings.py
     ├── urls.py
     └── wsgi.py
```

## Usage

* Runserver:

```
python manage.py runserver 0.0.0.0:8000
```

* Go to:

```
localhost:8000
```

* Upload a file (image, pdf, etc.) using the HTML button.
Nope, this project does not have styles (yet).

* The file is uploaded to root `/media/` as you can see on `settings.MEDIA_URL`.

## TODO

* Add basic styles.
* Responsive.
* Generate docker image.
* Generate kubernetes yaml. 