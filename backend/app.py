from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load your resources
with open('resources.json', 'r') as f:
    resources_en = json.load(f)

with open('resources_es.json', 'r') as f:
    resources_es = json.load(f)

@app.route('/resources', methods=['GET'])
def get_resources():
    lang = request.args.get('lang', 'en')  # Default to English if no lang provided
    category = request.args.get('category')

    # Choose the right language dataset
    if lang == 'es':
        data = resources_es
    else:
        data = resources_en

    # Filter by category if specified
    if category:
        filtered_resources = [r for r in data if r.get('category') == category]
        return jsonify(filtered_resources)
    else:
        return jsonify(data)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Server is running!"})

if __name__ == '__main__':
    app.run(debug=True)