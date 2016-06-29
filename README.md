# Biosensor

&nbsp;

## Introduction

Biosensor is a django based web app built as an open source project under a MIT license

&nbsp;

## Setup  

#### Requirements  
You need to have these installed on your development machine and on the server
- [python3](https://www.python.org)  
- [postgres](https://www.postgresql.org) (used for staging and production)
- [sqlite](https://www.sqlite.org/) (used for development only)
- [node](https://nodejs.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

#### Command line

`cd` into the project root dir  
`virtualenv -p python3 venv` *initialise python 3 virtual environment*  
`. venv/bin/activate` *start the virtual environment*  
`pip install -r requirements.txt` *install required python modules*  
`npm install` *install required node modules*  
`export DJANGO_SETTINGS_MODULE=biosensor.settings` *tell django where to find the configuration file*  
`./manage.py migrate` *initialise the postgress database*  
`./manage.py createsuperuser` *create admin user*  
`./manage.py runserver` *start the app*  

#### Environment variables

Be sure to set the following environment variables when setting up the app for staging or production:

`export DJANGO_ENV={development|staging|production}` *set up the app to run in development, staging or production mode*
`export SECRET_KEY=[random string of characters]` *a secret key used to provide cryptographic signing*  
`export DATABASE_URL=postgres://username:password@server:port/databasename` *database connection information*

#### Email

In order for email notifications to be sent out, the following environment variables need to be set:

`SMTP_SERVER` *the host to use for sending email*  
`SMTP_LOGIN` *password to use for the SMTP server defined in SMTP_SERVER*  
`SMTP_PASSWORD` *username to use for the SMTP server defined in SMTP_SERVER*  
`SMTP_PORT` *port to use for the SMTP server defined in SMTP_SERVER*  

&nbsp;

## Development

#### Frameworks and components used
- [Django](https://www.djangoproject.com) *python based web app framework*
- [Node](https://nodejs.org/) *javascript runtime*
- [NPM](https://www.npmjs.com) *javascript package manager*
- [Gulp](http://gulpjs.com) *build system*
- [Sass](http://sass-lang.com) *css preprocessor*
- [Bootstrap 4](http://v4-alpha.getbootstrap.com) *css framework*

#### Run command

`cd` into the project root dir and run
`. venv/bin/activate && ./manage.py runserver`

#### Database migations

If you make changes to one of the models, make sure to also migrate the database to reflect your changes.

`cd` into the project root dir and run  
`. venv/bin/activate`  
`./manage.py makemigrations` *create new migrations based on the changes you have made to your models.*  
`./manage.py migrate` *apply migrations to update the database*  

#### Update server

We recommend setting up continous deployment using github [webhooks](https://developer.github.com/webhooks/) so any changes pushed to master and/or production branch are automatically reflected on the server. 

&nbsp;

## Edit/update text/content

#### TODO: guide for setting up the CMS (content pages + frontpage text)

#### Menu

The menu is hard-coded within the div with the `navbar-nav` class in [base.html](https://github.com/Socialsquare/biosensor/blob/master/biosensor/templates/base.html) 

#### Frontpage video

Change the file ID e.g. `IvUU8joBb1Q` between `embed/` and `?` here on [this line](https://github.com/Socialsquare/biosensor/blob/master/biosensor/templates/index.html#L16) 

&nbsp;

## License

The MIT License (MIT)

Copyright © `2016` `Biotech Academy`

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
