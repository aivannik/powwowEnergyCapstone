# powwowEnergyCapstone

<<<<<<< HEAD
Daniel Updates for October 18th:

This week, I mainly focused on learning what data we had to work with and how to model that in a database.

We received access to the ETa data on Tuesday, and I read through the instructions to try to understand what it contianed. ETa is Evapotranspiration data and the Reference doc contained a lot of jargon that I will be speaking with our mentor Thomas about.

We did not yet receive the data for the other layers, but I did look up what data might potentially be in them. 
I found these two links and read through them:
https://water.ca.gov/LegacyFiles/groundwater/casgem/pdfs/CASGEM%20DWR%20GW%20Guidelines%20Final%20121510.pdf

https://fas.org/sgp/crs/misc/R44093.pdf

I also created a stub database:
CREATE TABLE stub( col1 int, PRIMARY KEY (col1) )

I wrote a stub script to read from this database as practice to know how to do it later. It’s still doesn’t work exactly. It is committed to my own branch.
=======
To run frontend:

```
cd frontend

npm install

npm start
```

To run backend, you need to install pipenv

These instructions assume that default python is python3. If the default is python2, then you need to run using pip3 and python3.

```
pip install pipenv

pipenv shell
```

Do all of this from within the pipenv shell:
```
pip install django

pip install djangorestframework 

pip install django-cors-headers

cd backend

python manage.py runserver
```

Type ```exit``` to exit the shell

To add a new model, start the pipenv shell and run the following:
```
cd backend

python manage.py startapp model_name_here
```


[Link to tutorial](https://scotch.io/tutorials/build-a-to-do-application-using-django-and-react)
>>>>>>> 52a6471d3be2c8fd85e290b1cc95a7c08b14647a
