# -*- coding: utf-8 -*-
__author__ = 'xu'

import os
from flask import Flask

app = Flask(__name__)

APP_ENV = 'dev'
_os_app_env = os.getenv('APP_ENV', APP_ENV)

if _os_app_env.lower() == 'dev':
    app.config.from_object('config')
    print('Running on DEV Env:')
elif _os_app_env.lower() in ('prod', 'test'):
    app.config.from_object('config')
    app.config.from_object('config_' + _os_app_env.lower())
    APP_ENV = _os_app_env.lower()
    print('Running on %s Env:' % _os_app_env.upper())
else:
    print('Wrong Env!')
    exit(1)

app.config["APP_ENV"] = APP_ENV

from . import models

@app.route('/')
def index():
    return 'You did it !!!'

# register api blueprint