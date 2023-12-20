from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_result

app = Flask(__name__)
CORS(app, resources={
    r'/submit': {
        'origins': ['http://localhost:5173', 'https://kdg391.github.io']
    }
})

@app.route('/submit', methods=['POST'])
def submit():
    payload = request.get_json()
    result = get_result(payload)

    return jsonify(result)

app.run(host='0.0.0.0')