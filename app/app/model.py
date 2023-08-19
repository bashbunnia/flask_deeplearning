"""
model.py: Functions related to Deep Learning model based on Keras.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


from tensorflow.keras.models import load_model
from skimage import transform, util
import numpy as np

from flask import current_app


def init_model():
    """Function that loads Deep Learning model.
    Returns:
      