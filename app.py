import os
from flask import Flask
app = Flask(__name__)

APP_MSG = os.environ.get('APP_MSG', 'World')

@app.route("/")
def hello():
  return f"Hello {APP_MSG}!\n"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
