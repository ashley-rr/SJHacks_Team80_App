from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load your resources
with open('resources.json', 'r') as f:
    resources = json.load(f)

@app.route('/resources', methods=['GET'])
def get_resources():
    category = request.args.get('category')
    if category:
        filtered_resources = [r for r in resources if r.get('category') == category]
        return jsonify(filtered_resources)
    else:
        return jsonify(resources)

if __name__ == '__main__':
    app.run(debug=True)