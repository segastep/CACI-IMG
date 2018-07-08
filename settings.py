import os
#SQLAlchemy settings
DB_URI='sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Adds overhead if true


#PATHS
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

#Logging conf path
LOGGING_CONFIG_FILE = os.path.join(ROOT_DIR, 'logging.conf')

