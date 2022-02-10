from flask import Flask, redirect, url_for, request, render_template, make_response, send_from_directory
from flask_mail import * 
from flask import jsonify
import json
import datetime
import pickle 
# from uritemplate.api import expand 

app = Flask(__name__)


if __name__ == '__main__':
   app.run(host = '192.168.85.182', debug = True, port=5000)
