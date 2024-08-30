from .extensions import socketio

def send_notification(message):
    socketio.emit('notification', {'message': message})
