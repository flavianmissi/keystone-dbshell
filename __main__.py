import os
import sqlalchemy as sa
from keystone import config
from keystone.common import sql

config.configure()
config.CONF(args=[], project='keystone')

os.environ['PYTHONINSPECT'] = 'True'
conn = os.env.get("DB_CONNECTION", 'mysql://keystone:KEYSTONE_DBPASS@localhost/keystone')
engine = sa.create_engine(conn, echo=True)
session = sql.get_session()
