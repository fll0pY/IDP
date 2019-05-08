from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
