#!/bin/bash
USER=u0_a270                                   	# the user to run as
NAME="guessr"                                  		# Name of the application
PROJECTDIR=/data/data/com.termux/files/home/xcode/guess_ssr             				# Django project directory
SOCKFILE=/data/data/com.termux/files/home/xcode/guess_ssr/unicorn.sock  		# we will communicte using this unix socket
GROUP=$USER                                     		# the group to run as
NUM_WORKERS=3                                     	# how many worker processes should Gunicorn spawn

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $PROJECTDIR
source /data/data/com.termux/files/home/xcode/guess_ssr/.venv/bin/activate
#export DS_ENVIRONMENT=production
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$PROJECTDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /data/data/com.termux/files/home/xcode/guess_ssr/.venv/bin/uvicorn --app-dir backend main:app --reload  
