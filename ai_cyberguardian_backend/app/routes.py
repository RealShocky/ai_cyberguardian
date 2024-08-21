from flask import Blueprint, request, jsonify
from .ai import perform_analysis

ai_blueprint = Blueprint('ai', __name__)

@ai_blueprint.route('/ai-analysis', methods=['POST'])
def ai_analysis():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    text = data['text']
    result = perform_analysis(text)
    return jsonify({"result": result}), 200
