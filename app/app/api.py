"""
api.py: api views used by Flask server.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


from flask import Blueprint, jsonify, request

from skimage.io import imread
import io

from .model import *


api = Blueprint('api', __name__)

@api.route("/predictlabel", methods=["POST"])
def predict():
    # result dictionary that will be returned from the view
    result = {"success