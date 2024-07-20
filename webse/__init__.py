from flask import Flask, jsonify, request 
from flask_cors import CORS
import uuid

application = Flask(__name__)

application.config.from_object(__name__)

CORS(application, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

from webse.forward_home.routes import forward_home

application.register_blueprint(forward_home)