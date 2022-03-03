#!/usr/bin/env bash
export FLASK_APP="mainapp.py";
echo $FLASK_APP
flask run
flask db init
flask db migrate
#python manager.py db upgrade
#flask run --host=0.0.0.0