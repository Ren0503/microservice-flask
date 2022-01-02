import os
import json
from flask import make_response
from werkzeug.wrappers import response


def root_dir():
    """ Returns root director for this project """
    return os.path.dirname(os.path.realpath(__file__ + '/..'))


def nice_json(arg):
    response = make_response(json.dump(arg, sort_keys=True, indent=4))
    response.headers['Content-Type'] = "application/json"
    return response