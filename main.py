from flask import Flask
import numpy as np
from sklearn.preprocessing import Binarizer
import json


app = Flask(__name__)


@app.route("/")
def hello_world():
    age = np.array([[6],[12],[18],[20],[36],[65]])
    arr_list = age.tolist()

# Serialize the list to JSON
    json_data = json.dumps(arr_list)
    return json_data