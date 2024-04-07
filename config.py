import os
from dotenv import load_dotenv
load_dotenv()

class ApplicationConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ['SECRET_KEY']
    USERNAME = os.environ['USERNAME']
    PASSWORD= os.environ['PASSWORD']
    ENDPOINT = os.environ['ENDPOINT']
    DATABASE = os.environ['DBNAME']
    SQLALCHEMY_ECHO = True
    
    SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{ENDPOINT}:3306/{DATABASE}"

