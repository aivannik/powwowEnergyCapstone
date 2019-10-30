### Prototype Class builder for database classes

- The python script ClassBuilder.py requires a database.ini file to connect to
the psql server
  - From this tutorial: http://www.postgresqltutorial.com/postgresql-python/connect/
  - This was the syntax for file
  '[postgresql]
  host=
  database=
  user=
  password='
  - Host, user, password provided in the professor's email
  - database is "db1"

- As a test run, this script connects to the psql database db1 and searches for
entries that have a precipitation (prcp is the column name) value that is
greater than 0
- Those entires are stored in a temporary array and printed out  




## To run
`python3 ClassBuilder.py`

## Troubleshoot
- I had problems getting pip3 to install psycopg2
- Using cygwin on windows, I needed to install some or all of these packages:
  - python3
  - Pip3
  - psql
  - libpq-dev
  - python3-devel
