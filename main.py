#-*- coding: utf-8 -*-
import os
import logging

from flask import Flask
from flask import render_template
from flask import request

DEBUG = os.getenv('SERVER_SOFTWARE', '').startswith('Development/')

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

"""
from flask import abort, jsonify

# examples
@app.route('/tags', methods=['POST'])
  request.json
  request.form['name']
  request.args.get('name')
  return jsonify(items=items)

@app.route('/tags/<string:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
  return abort(400)
"""

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
