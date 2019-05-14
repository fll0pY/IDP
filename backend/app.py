from typing import List, Dict
from flask import Flask
import mysql.connector
import json

# Initialize the app
app = Flask(__name__)

# Load the config file
app.config.from_object('config')

@app.route('/')
def hello_world():
    return 'Hello, Wold!'

def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
