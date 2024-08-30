from flask import Blueprint, request, jsonify
from .ai import perform_analysis, add_data_source
import logging

ai_blueprint = Blueprint('ai_blueprint', __name__)
notification_blueprint = Blueprint('notification_blueprint', __name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@ai_blueprint.route('/ai-analysis', methods=['POST'])
def ai_analysis():
    data = request.get_json()
    text = data.get('text')
    
    if not text or len(text.strip()) == 0:
        logger.error("Input validation failed: Text is missing or empty.")
        return jsonify({"error": "Input text cannot be empty."}), 400

    try:
        result, updated_history = perform_analysis(text)
        return jsonify({"result": result, "history": updated_history}), 200
    except Exception as e:
        logger.error(f"Error during AI analysis: {e}")
        return jsonify({"error": "An error occurred during analysis."}), 500

@ai_blueprint.route('/add-data-source', methods=['POST'])
def add_data_source_route():
    data = request.get_json()
    source_name = data.get('source_name')
    data_content = data.get('data')

    if not source_name or not isinstance(source_name, str):
        logger.error("Input validation failed: Source name is missing or invalid.")
        return jsonify({"error": "Source name must be a non-empty string."}), 400

    if not isinstance(data_content, dict):
        logger.error("Input validation failed: Data content is not a dictionary.")
        return jsonify({"error": "Data must be a dictionary."}), 400

    try:
        new_source = add_data_source(source_name, data_content)
        return jsonify({"message": "Data source added successfully."}), 201
    except Exception as e:
        logger.error(f"Error adding data source: {e}")
        return jsonify({"error": "An error occurred while adding the data source."}), 500
