# formaloo-sdk-django-test


A simple ptoject to test formaloo python sdk


# Installation

pip install -r requirements.txt

git clone `https://github.com/alisoltanics/formaloo-python.git`

cd to sdk project and run:

python setup.py install

# Run
Create some actions for create and like posts in formaloo's dashboard, then add slug of actions in this file: blog/constants.py

`export FORMALOO_CLIENT_KEY = 'YOUR_FORMALOO_CLIENT_KEY'`

`export FORMALOO_CLIENT_SECRET = 'YOUR_FORMALOO_CLIENT_SECRET'`

python manage.py migrate

python manage.py runserver

# Run tests
`python manage.py test`

# Run view tests
`python manage.py test --tag=ViewName`

example: `python manage.py test --tag=PostViewSet`

# Flow
Every time that we create an user, a customer will create in formaloo, and when user likes or creates a post, we will create an activity for user in formaloo and give score to user (based on type of posts, `text`, `image`, `song`).

