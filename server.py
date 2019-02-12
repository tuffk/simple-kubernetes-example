"""simple flask API examples"""
from os import getenv
from flask import Flask, request

app = Flask(__name__)

@app.route("/<string:name>", methods=["GET"])
def hello_get(name: str) -> str:
    """GET Method that returns an interpolated string with the parameter

    Args:
        name(string): name to be interpolated in the response

    Retuns:
        string: string response
    """
    return f"Hello {name}!"


@app.route("/", methods=["POST"])
def hello_post(name: str) -> str:
    """POST Method that returns an interpolated string with the parameter

    Parameter:
        {"name": string}

    Retuns:
        string: string response
    """
    data = request.json
    name = data['name']
    return f"Hello {name}!"


@app.route("/env", methods=["GET"])
def hello_env() -> str:
    """GET Method that returns an interpolated string with the environment variable

    Retuns:
        string: string response
    """
    name = getenv("HELLO_ENV", "no env")
    return f"Hello {name}!"
