import psycopg2
from psycopg2 import sql
import os

# Database connection settings
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'ai_cyberguardian_db')
DB_USER = os.getenv('DB_USER', 'cyber_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'admin_Konnann2218')
DB_PORT = os.getenv('DB_PORT', '5432')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'postgres')  # Default DB to connect initially
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')  # Superuser to create DB
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'admin_Konnann2218@1')  # Superuser password

# Connect to PostgreSQL server
conn = psycopg2.connect(dbname=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=DB_HOST, port=DB_PORT)
conn.autocommit = True  # Allow database creation

# Create a cursor to execute commands
cur = conn.cursor()

# Create the new database
cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))

# Create a new user with password
cur.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s").format(sql.Identifier(DB_USER)), [DB_PASSWORD])

# Grant all privileges on the new database to the new user
cur.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(sql.Identifier(DB_NAME), sql.Identifier(DB_USER)))

# Close communication with the PostgreSQL database server
cur.close()
conn.close()

print(f"Database {DB_NAME} and user {DB_USER} created successfully.")
