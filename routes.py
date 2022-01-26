from flask import Flask, jsonify, request
import controller

app = Flask(__name__)


@app.route('/puntajes', methods=["GET"])
def get_puntajes():
    puntajes = controller.get_puntajes()
    return jsonify(puntajes)


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8000, debug=False)
