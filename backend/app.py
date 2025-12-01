from flask import Flask, request, jsonify
from flask_cors import CORS
from llm_api import poem_to_landscape
from model import generate_painting 

app = Flask(__name__)
CORS(app)

@app.get("/api/ping")
def ping():
    return jsonify({"msg": "backend is ok"})

@app.post("/api/generate")
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    improved_prompt = poem_to_landscape(prompt)

    image_base64 = generate_painting(improved_prompt)

    return jsonify({
        "prompt": improved_prompt,
        "image": image_base64
    })

if __name__ == "__main__":
    app.run(port=5000)
