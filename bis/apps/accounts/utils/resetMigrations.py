find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
find . -name __pycache__ -type d -print0|xargs -0 rm -r --
python3 manage.py migrate --run-syncdb
