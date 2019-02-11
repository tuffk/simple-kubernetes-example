from flask import Flask, request

app = Flask(__name__)

@app.route("/<string:name>", methods=["GET"])
def hello_get(name):
    """GET Method that returns an interpolated string with the parameter

    Args:
        name(string): name to be interpolated in the response

    Retuns:
        string: string response
    """
    return f"Hello {name}!"


@app.route("/", methods=["POST"])
def hello_post(name="world"):
    """POST Method that returns an interpolated string with the parameter

    Parameter:
        {"name": string}

    Retuns:
        string: string response
    """
    data = request.json
    return f"Hello {data['name']}!"
