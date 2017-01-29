"""
    Set up defaults and read sentinel.conf
"""
import sys
import os
from darksilk_config import DarkSilkConfig

sentinel_cfg = DarkSilkConfig.tokenize('sentinel.conf')

def get_darksilk_conf():
    home = os.environ.get('HOME')

    darksilk_conf = os.path.join(home, ".darksilk/darksilk.conf")
    if sys.platform == 'darwin':
        darksilk_conf = os.path.join(home, "Library/Application Support/DarkSilk/darksilk.conf")

    darksilk_conf = sentinel_cfg.get('darksilk_conf', darksilk_conf)

    return darksilk_conf

def get_network():
    return sentinel_cfg.get('network', 'mainnet')

def get_db_conn():
    import peewee
    env = os.environ.get('SENTINEL_ENV', 'production')

    # default values should be used unless you need a different config for development
    db_host = sentinel_cfg.get('db_host', '127.0.0.1')
    db_port = sentinel_cfg.get('db_port', None)
    db_name = sentinel_cfg.get('db_name', 'sentinel')
    db_user = sentinel_cfg.get('db_user', 'sentinel')
    db_password = sentinel_cfg.get('db_password', 'sentinel')
    db_charset = sentinel_cfg.get('db_charset', 'utf8mb4')
    db_driver = sentinel_cfg.get('db_driver', 'mysql')

    if (env == 'test'):
        db_name = "%s_test" % db_name

    peewee_drivers = {
        'mysql': peewee.MySQLDatabase,
        'postgres': peewee.PostgresqlDatabase,
        'sqlite': peewee.SqliteDatabase,
    }
    driver = peewee_drivers.get(db_driver)

    dbpfn = 'passwd' if db_driver == 'mysql' else 'password'
    db_conn = {
        'host': db_host,
        'user': db_user,
        dbpfn: db_password,
    }
    if db_port:
        db_conn['port'] = int(db_port)

    if driver == peewee.SqliteDatabase:
        db_conn = {}

    db = driver(db_name, **db_conn)

    return db

darksilk_conf = get_darksilk_conf()
network = get_network()
db = get_db_conn()
