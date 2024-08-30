from .extensions import db

class Threat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    analysis = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class DataSource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    api_url = db.Column(db.String(255), nullable=False)
    api_key = db.Column(db.String(255), nullable=True)  # If applicable
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class UserFeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.String(50), nullable=False)
    conversation_history = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def save(self):
        db.session.add(self)
        db.session.commit()