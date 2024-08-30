import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ai_cyberguardian.db'  # This will create a .db file in your project root
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # Ensure this is set in your environment
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # Ensure this is set if you're using this API
