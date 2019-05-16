# config.py

# Enable Flask's debugging features. Should be False in production
DEBUG = True

SQLALCHEMY_DATABASE_URI="mysql+mysqldb://root:root@db/idp"
SQLALCHEMY_TRACK_MODIFICATIONS = False