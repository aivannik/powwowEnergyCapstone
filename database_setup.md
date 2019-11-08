1. See Bryan for env variables and Django super user credentials
2. 

psql --port=5432 --host=169.231.234.213 --username=ubuntu --dbname=db1 -W


If sshing:
sudo -i -u postgres

Checkout database db1:
\c db1

Read a psql cheatsheet

To restart:
sudo service postgresql restart]

In pipenv shell:
pip install python-dotenv