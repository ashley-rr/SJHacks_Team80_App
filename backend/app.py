from flask import Flask, jsonify

import json

app = Flask(__name__)

# Load your JSON database
with open('resources.json', 'r') as f:
    resources = json.load(f)

@app.route('/resources', methods=['GET'])
def get_resources():
    return jsonify(resources)

if __name__ == '__main__':
    app.run(debug=True)