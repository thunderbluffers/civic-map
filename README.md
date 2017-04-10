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

## Install Miniconda
```bash
conda list --name civic-map || conda create --name civic-map -y python
source activate civic-map
pip install -r requirements.txt
python manage.py runserver
```

## For Windows + Pycharm:
  Edit configurations (google it) for manage.py and add `runserver` to `Script parameters`.
  To run/debug, right-click `manage.py` from the project solution and click run/debug.

## Useful commands
0. `python manage.py shell -i ipython`
0. `source .venv/bin/activate`
0. `python manage.py createsuperuser`
