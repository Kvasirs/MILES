from flask import redirect, url_for, render_template, abort, send_from_directory, send_file, jsonify, request
from flask import Flask

from gevent.pywsgi import WSGIServer
import threading
import random
import json
import time
import os
import io

from simplifier import simplifier
from simplifier import models
from simplifier import config

#Create app
app = Flask(__name__,static_url_path='')
app.debug = False

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/ai_request/', methods=['GET', 'POST'])
def ai_request():
    
    if request.method == 'POST':

        text = request.form.get('input')

        print(text)

        output = simplifier.simplify_text_html(text)

        return jsonify({"output": output})


if __name__ == "__main__":

    models.embeddings = models.load_embeddings(config.lang)
    http_server = WSGIServer(('0.0.0.0', 80), app)    
    print("Loaded as HTTP Server on port 80, running forever:")
    http_server.serve_forever()
