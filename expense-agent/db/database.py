import os
import psycopg2
from dotenv import load_dotenv  
load_dotenv()  # Charger les variables d'environnement depuis le fichier .env


def get_connection():

    database_url = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(database_url)

    return conn