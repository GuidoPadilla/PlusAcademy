REM Instalar coverage mediante el comando pip install coverage

coverage run --source='.' manage.py test myapp

coverage report