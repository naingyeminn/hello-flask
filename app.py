import os
from flask import Flask
app = Flask(__name__)

APP_MSG = os.environ.get('HOSTNAME', 'hello-flask')

@app.route("/")
def hello():
  return f"Welcome to {APP_MSG}!\n This is a new day!\n"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
