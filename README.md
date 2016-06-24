#Biosensor

##How to setup  
install postgres database
or use the one from heroku by exporting environment variables.

###Requirements  
python3  
postgres  
node  
virtualenv  


###First time
```
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
npm install
export DJANGO_SETTINGS_MODULE=biosensor.settings
./manage.py migrate
./manage/py runserver
```

###Every time
```
. venv/bin/activate && ./manage.py migrate && ./manage.py runserver
```
