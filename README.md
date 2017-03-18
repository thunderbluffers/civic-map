# Civic Map

## Requirements
- python 3.5
- pip 9
- [mysqlclient](http://rosindex.github.io/d/libmysqlclient-dev)

## Install
1. Clone the project
2. Copy `.env.example` to `.env` and update environment variables:
  * `DB_NAME` - Database name
  * `DB_USER` - Database user
  * `DB_PASSWORD` - Database password
  * `DB_HOST` - Database host
3. Run `make install`
4. Launch the project running:
  `make run`
  or
  `source .venv/bin/activate; python manage.py runserver`

## Useful commands
0. `python manage.py shell -i ipython`
0. `source .venv/bin/activate`
0. `python manage.py createsuperuser`
