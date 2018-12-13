# -*- coding: utf-8 -*-

"""实例化 peewee Database
"""

from flask_peewee.db import Database
from app import app

db = Database(app)