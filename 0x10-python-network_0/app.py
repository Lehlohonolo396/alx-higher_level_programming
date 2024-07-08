from flask import (Flask,
                   redirect, request,
                   url_for, jsonify,
                   make_response, abort,
                   Response)
from functools import wraps

app = Flask(__name__)
app.url_map.strict_slashes = False

def allowed_methods(methods=['GET']):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not request.method in methods:
                return abort(405)  # Method Not Allowed
            return function(*args, **kwargs)
        return wrapper
    return decorator


@app.route('/')
def route_0():
    return f'123456789\n', 200


@app.route('/route_1')
def route_1():
    return f'Route 2\n'


@app.route('/route_3', methods=['DELETE'])
def route_3():
    return f"I'm a DELETE request\n"


@app.route('/route_4', methods=['PUT'])
@allowed_methods(['PUT'
