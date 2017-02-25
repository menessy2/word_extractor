import os
from Crypto.PublicKey import RSA


dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')



MYSQL_USER = os.environ.get('MYSQL_USER','user1')
MYSQL_PASS = os.environ.get('MYSQL_PASS','pass1')
MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME','test_octopus_db2')
MYSQL_HOST = os.environ.get('MYSQL_HOST','localhost')
MYSQL_PORT = str(os.environ.get('MYSQL_PORT','3306'))


pub_key_file = open(dirname+'/keys/public.pem','r')
private_key_file = open(dirname+'/keys/private.key','r')

ASYMMETRIC_PUB_KEY = RSA.importKey(pub_key_file.read())
ASYMMETRIC_PRIVATE_KEY = RSA.importKey(private_key_file.read())

pub_key_file.close()
private_key_file.close()

HASH_SALT = 'testhash'