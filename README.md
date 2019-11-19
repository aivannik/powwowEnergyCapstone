# powwowEnergyCapstone


NEW Instructions:

1. Install Docker. (For Windows, install docker toolbox)

2. Get the .env file and put it in the root

```
$ docker-compose up --build
```

To see on Windows:
```
192.168.99.100:5000 for backend
192.168.99.100:3000 for frontend
```

To see on Mac:
```
localhost:5000 for backend
localhost:3000 for frontend
```


OLD INSTRUCTIONS: 
```
$ cd prod_server
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```
Do all of this from within the virtualenv shell:
```
$ pip3 install Flask
$ pip3 install flask_sqlalchemy
$ pip3 install flask_script
$ pip3 install flask-cors
$ pip3 install flask_migrate
$ pip3 install psycopg2-binary
$ pip3 install python-dotenv
$ export APP_SETTINGS=config.DevelopmentConfig
$ export DATABASE_URL=postgresql://localhost/db1  // DONT DO THIS STEP IF YOU WANT TO CONNECT TO THE REAL DB. Change the URL
$ cd ../
$ python3 prod_server/manage.py runserver
```

Type ```deactivate``` to exit the shell

NOTE: In order to run the server, these exports must be executed each time the virtualenv shell is activated.
```
$ export APP_SETTINGS="config.DevelopmentConfig"
$ export DATABASE_URL="postgresql://localhost/db1"
```

frontend packages: 
```
cd frontend
npm install 
```

To Start the Frontend:
Make sure you're in the frontend directory
```
npm start
```
[Link to tutorial](https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react)
