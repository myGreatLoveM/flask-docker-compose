from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    def __init__(self):
        load_dotenv()
        self.SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config()
