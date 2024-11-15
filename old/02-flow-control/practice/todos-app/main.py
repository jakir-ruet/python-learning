from dotenv import load_dotenv
from handlers.handler import handleUser

DOT_ENV = "./config/.env"

load_dotenv(DOT_ENV)
handleUser()
