Biosensor
=========

development
===========
   install postgres database
   or use the one from heroku by exporting environment variables.

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    npm install
    bower install
    export DJANGO_SETTINGS_MODULE=biosensor.settings
    ./manage.py migrate
    ./manage/py runserver
