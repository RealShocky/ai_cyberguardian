import openai
from flask import current_app, jsonify, request
import logging
from .models import DataSource
from .extensions import db

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def perform_analysis(text):
    if not text or len(text.strip()) == 0:
        logger.error("Invalid input: Text is empty or only whitespace.")
        raise ValueError("Input text cannot be empty.")
    
    logger.info(f"Performing AI analysis on the text: {text}")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=150
    )
    
    result = response.choices[0].text.strip()
    logger.info(f"AI analysis result: {result}")
    return result

def add_data_source(source_name, data):
    if not source_name or not isinstance(source_name, str):
        logger.error("Invalid source_name: Must be a non-empty string.")
        raise ValueError("Source name must be a valid non-empty string.")
    
    if not isinstance(data, dict):
        logger.error("Invalid data: Must be a dictionary.")
        raise ValueError("Data must be a dictionary.")

    logger.info(f"Adding data source: {source_name} with data: {data}")
    data_source = DataSource(name=source_name, data=data)
    db.session.add(data_source)
    db.session.commit()
    logger.info("Data source added successfully.")
    return data_source
