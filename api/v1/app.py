#!/usr/bin/python3
""" App """

from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.errorhandler(404)
def handle_404(exception):
    """
    Handles 404 error
    return: 404 json
    """
    data = {
            "error": "Not found"
    }

    response = jsonify(data)
    response.status_code = 404

    return(response)


@app.teardown_appcontext
def teardown(exception):
    """ Teardown function """
    storage.close()


if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
