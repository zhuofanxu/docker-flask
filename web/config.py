# -*- coding: utf-8 -*-
__author__ = 'xu'

# the host use the alias of database_network `database`

DATABASE = {
    'user': 'test',
    'name': 'test',
    'engine': 'peewee.PostgresqlDatabase',
    'host': 'database',
    'password': 'lzsb'
}

ADMIN_URL = "/admin"
BRANDING = "Docker-Flask"