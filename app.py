from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, This is my first pipeline..!'

# Run the application
if __name__ == '__main__':
    # Expose the app on all IP addresses and set port to 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
