import os
from flask import Flask
app = Flask(__name__)

APP_HOSTNAME = os.environ.get('HOSTNAME', 'hello-flask')

@app.route("/")
def hello():
  return f"<h1>Welcome to {APP_HOSTNAME}</h1>\n <h2>This is a new day!</h2>\n"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
