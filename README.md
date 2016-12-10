# MP -Mejorpromedio

## Getting Started

Mejorpromedio Web Application
=======================

Instruction to run and use the mejor promedio web Application

Setup
--------

First you should have python, pip and virtualenv installed in OS x, for that please follow this tutorial(For python 2):

[osx tutorial](https://hackercodex.com/guide/python-development-environment-on-mac-osx/)


Then pull the repository

```
#!bash
   
$ git clone git@bitbucket.org:mp/mp.git

```

Move into the directory, setup virtualenv and install requirements


```
#!bash
   
$ cd mp/
$ virtualenv mysiteenv
$ source mysiteenv/bin/activate
$ pip install -r requirements.txt
#if pg_config not found, execute: brew install postgresql
$ cd mp/

```

```
#!bash
   
#To know online users using the cache system do:
$pip install python-memcached
#As for installing memcached itself, it depends on the platform you are on.



#Windows - http://pureform.wordpress.com/2008/01/10/installing-memcache-on-windows-for-php/

#OS X 
$brew install memcached
#Debian/Ubuntu
$sudo apt-get install memcached
#On OS X/Linux, just run memcached in the command line.

#start memcached in server and local with:
$memcached start

Everything is installed, now we need to setup and run django


$export DJANGO_SETTINGS_MODULE=mp.settings.local
$ cd mp/
$ python manage.py migrate
$ python manage.py runserver
Now you have a django server running, got to your browser and open this url http://127.0.0.1:8000

Test
----

to run the test after you make a change do this:
$ python manage.py test

```

Deploy in the server
-------------------

```
#!bash


When you have a change, you can commit it on your local machine, for that read this tutorial:

[How to commit and push in Git](https://backlogtool.com/git-guide/en/intro/intro1_1.html)

$git status
$git add --all .
git status
git commit -m "message"
git push


```
Then you should log into the server, pull and reload the daemons like this:
```

$ ssh deploy@104.131.180.80
$ cd mp/mp/
$ git pull
$ sudo supervisorctl restart all

#run this if mails are not ended this support celery to send mail using django_celery_mail plugin, check how to add rabbitmq to supervisor:
#export PATH=$PATH:/usr/local/sbin
# sudo rabbitmq-server 

# do this only if you modified some static content(js, css)
# need to have the virtualenv activated (source bin/activate)
$ export DJANGO_SETTINGS_MODULE=mp.settings.production
$ python manage.py collectstatic

```