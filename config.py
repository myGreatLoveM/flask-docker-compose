from dotenv import load_dotenv
import os

load_dotenv()



# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_HOST = os.getenv('DB_HOST')
# DB_NAME = os.getenv('DB_NAME')


class Config:
    def __init__(self):
        load_dotenv()
        self.SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False

# Singleton instance
config = Config()
