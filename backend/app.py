from flask import Flask, request, jsonify
from flask_cors import CORS
from llm_api import poem_to_landscape
from model import generate_painting 

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Welcome to the Painting Generator API"

@app.route('/api/ping')
def ping():
    return jsonify({"msg": "backend is fine"})

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    prompt = poem_to_landscape(text)

    image = generate_painting(prompt)

    return jsonify({
        'prompt': prompt,
        'image': image
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
