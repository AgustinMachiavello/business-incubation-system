# Project 'OpenSeed'
Online incubation administration system.


## Developer team and contact
Petra Sánchez - petrasanchez83@gmail.com
Juan Pablo Luzuriaga - jp.luzu@gmail.com
Nicolás Machado - nicomach99@gmail.com
Agustín Machiavello - agmachiavello@gmail.com


## Motivation
Presented as the 2021 computer science final career project under the name of 'OpenSeed'.


## Rights and Licence
MIT License. 

You are free to do whatever you want :)


## Useful commands 💻

### Reset migrations

##### We do not recommmend reseting your migrations unless you know what your are doing. It may cause unconsistency problems on your database.


This is based on the following [Online tutorial.](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)


Go through each of your projects apps migration folder and remove everything inside, except the ```__init__.py``` file. 

Or **if you are using a unix-like OS** you can run the following script (inside your project dir):

```find . -path "*/migrations/*.py" -not -name "__init__.py" -delete```
```find . -path "*/migrations/*.pyc"  -delete```

### Remove caché
```find . -name __pycache__ -type d -print0|xargs -0 rm -r --```

### Sync database
```python3 manage.py migrate --run-syncdb```

###### thanks for reading :)
