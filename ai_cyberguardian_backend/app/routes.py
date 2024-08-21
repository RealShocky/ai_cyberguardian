# app/routes.py
from flask import Blueprint, request, jsonify
from .ai import perform_analysis

ai_blueprint = Blueprint('ai', __name__)

@ai_blueprint.route('/ai-analysis', methods=['POST'])
def ai_analysis():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({"error": "Text is required"}), 400

    try:
        result = perform_analysis(text)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
