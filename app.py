from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TechVJ'

def run_flask_app():
    while True:
        try:
            print("🚀 Flask app is running...")
            app.run(debug=False)  # Disable debug mode for production-like behavior
        except Exception as e:
            print(f"⚠️ Flask app crashed: {e}")
            time.sleep(5)  # Wait for 5 seconds before restarting

if __name__ == "__main__":
    run_flask_app()
