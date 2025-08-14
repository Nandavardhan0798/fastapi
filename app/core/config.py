<<<<<<< HEAD
import os
from dotenv import load_dotenv

class Settings:
    PROJECT_NAME = "Capstone_Project"
    API_KEY = os.getenv("API_KEY", "demokey")
    JWT_KEY = os.getenv("JWT_KEY", "secret")
    REDIS_URL =os.getenv("REDIS_URL", "redis://localhost.6379")
    JWT_ALGORITHM = "HS256"
    MODEL_PATH = 'app/models/mdel.pkl'

settings = Settings()
=======
import os
from dotenv import load_dotenv

class Settings:
    PROJECT_NAME = "Capstone_Project"
    API_KEY = os.getenv("API_KEY", "demokey")
    JWT_KEY = os.getenv("JWT_KEY", "secret")
    REDIS_URL =os.getenv("REDIS_URL", "redis://localhost.6379")
    JWT_ALGORITHM = "HS256"
    MODEL_PATH = 'app/models/mdel.pkl'

settings = Settings()
>>>>>>> e6cb0c2e6243c8d56831456aaf99109a2cdeeb58
