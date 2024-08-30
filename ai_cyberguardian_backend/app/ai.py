import openai
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback_text = db.Column(db.String(500))
    rating = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Define DataSource model
class DataSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(500))
    added_on = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
with app.app_context():
    db.create_all()

def perform_analysis(text, conversation_history=None):
    if not text or len(text.strip()) == 0:
        logger.error("Invalid input: Text is empty or only whitespace.")
        raise ValueError("Input text cannot be empty.")
    
    logger.info(f"Performing AI analysis on the text: {text}")

    # Maintain a conversation context if provided
    messages = [
        {"role": "system", "content": "You are a cybersecurity analysis assistant. Your task is to analyze potential threats in the user's message and provide detailed, actionable insights."},
    ]

    # If conversation history exists, include it
    if conversation_history:
        messages.extend(conversation_history)
    
    # Append the current user input
    messages.append({"role": "user", "content": text})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=300,  # Increased tokens for more detailed responses
            temperature=0.7,  # Adjusting temperature for balanced creativity and coherence
            top_p=0.9,        # Using nucleus sampling to ensure diversity in response
            n=1,              # Number of responses to generate
            stop=None,        # Define stopping criteria if needed
        )

        result = response.choices[0].message['content'].strip()
        logger.info(f"AI analysis result: {result}")

        # Return the result along with the updated conversation history
        return result, messages

    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        raise RuntimeError("Error during AI analysis") from e

# Function to add a new data source
def add_data_source(name, url):
    logger.info(f"Adding new data source: {name}, {url}")
    new_source = DataSource(name=name, url=url)
    db.session.add(new_source)
    db.session.commit()

# Route for AI analysis
@app.route('/ai-analysis', methods=['POST'])
def ai_analysis():
    data = request.get_json()
    text = data.get('text', '')
    conversation_history = data.get('history', [])

    try:
        result, updated_history = perform_analysis(text, conversation_history)
        return jsonify({'result': result, 'history': updated_history}), 200
    except Exception as e:
        logger.error(f"Error during AI analysis: {e}")
        return jsonify({'error': str(e)}), 500

# Route for submitting feedback
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    feedback_text = data.get('feedback', '')
    rating = data.get('rating', 5)  # Default rating is 5

    if not feedback_text:
        return jsonify({'error': 'Feedback text cannot be empty.'}), 400

    feedback = Feedback(feedback_text=feedback_text, rating=rating)
    db.session.add(feedback)
    db.session.commit()

    logger.info(f"Received feedback: {feedback_text} with rating {rating}")

    return jsonify({'message': 'Feedback submitted successfully!'}), 200

# Route for adding data source
@app.route('/add-data-source', methods=['POST'])
def add_data_source_route():
    data = request.get_json()
    name = data.get('name', '')
    url = data.get('url', '')

    if not name or not url:
        return jsonify({'error': 'Both name and URL of the data source are required.'}), 400

    try:
        add_data_source(name, url)
        return jsonify({'message': 'Data source added successfully!'}), 200
    except Exception as e:
        logger.error(f"Error adding data source: {e}")
        return jsonify({'error': str(e)}), 500

# Route for getting feedback metrics
@app.route('/feedback-metrics', methods=['GET'])
def feedback_metrics():
    total_feedback = Feedback.query.count()
    average_rating = db.session.query(db.func.avg(Feedback.rating)).scalar()

    metrics = {
        'total_feedback': total_feedback,
        'average_rating': average_rating
    }

    logger.info(f"Feedback metrics: {metrics}")

    return jsonify(metrics), 200

if __name__ == '__main__':
    app.run(debug=True)
