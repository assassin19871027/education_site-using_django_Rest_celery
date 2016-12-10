#!/bin/bash
 
NAME="mp" # Name of the application
APPDIR=/home/deploy/mp/mp/ # Django project directory
USER=${1:-deploy} # the user to run as
GROUP=${2:-deploy}
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
#DJANGO_SETTINGS_MODULE=settings # which settings file should Django use
 
 
echo "Starting $NAME"
 
# Activate the virtual environment
cd $APPDIR
source ../bin/activate
export PYTHONPATH=$APPDIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=mp.settings.production


# Create the run directory if it doesn't exist
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn \
-b 127.0.0.1:4003 \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=debug mp.wsgi