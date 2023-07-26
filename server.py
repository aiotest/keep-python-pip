import os
from flask import Flask, render_template
import sys


app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Python version", flush=True)
    print(sys.version, flush=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
