# Delete all migration files
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# If using SQLite locally
rm -f db.sqlite3


# First create accounts app migration
python manage.py makemigrations accounts

# Then create other migrations
python manage.py makemigrations

# Apply all migrations
python manage.py migrate