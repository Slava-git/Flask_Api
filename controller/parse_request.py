
from flask import request

def get_request_data():
    res = {}
    data = request.form
    for key in data:
        res[key] = data[key]
    return res

