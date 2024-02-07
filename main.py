from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)

# Set a secret key for session management
app.config['SECRET'] = "secret"

# Create a SocketIO instance, allowing cross-origin requests from any domain ('*')
socketio = SocketIO(app, cors_allowed_origins="*")

# Define a SocketIO event handler for the 'message' event
@socketio.on('message')
def handle_message(message):
    # Broadcast the received message to all connected clients
    send(message, broadcast=True)

# Define a route for the main index page
@app.route('/')
def index():
    # Render the HTML template for the index page
    return render_template("index.html")

# Run the SocketIO server if the script is executed directly
if __name__ == "__main__":
    # Start the Flask app with the SocketIO server
    socketio.run(app, host="localhost")
