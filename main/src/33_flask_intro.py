"""
Flask Introduction: Building a Simple Web App

Flask is a lightweight web framework for Python.
This script creates a basic web server.
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello():
    return "Hello, World! Welcome to your first Flask app."

# Define another route
@app.route('/about')
def about():
    return "This is a simple Python data science tutorial project."

# Run the app
if __name__ == '__main__':
    print("Starting Flask app... Visit http://127.0.0.1:5000/")
    app.run(debug=True)