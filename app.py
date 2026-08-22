from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This will help us prove which environment is running later
    env_name = os.environ.get('ENV_NAME', 'Local Development')
    return f"Hello! This is running in the {env_name} environment - Testing."

if __name__ == '__main__':
    from waitress import serve
    # We use 8080 as a default test port
    print("Server starting on port 8080...")
    serve(app, host='0.0.0.0', port=8080)