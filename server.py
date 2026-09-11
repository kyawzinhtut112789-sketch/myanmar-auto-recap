from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Myanmar Auto Recap Backend is working!"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.route("/test-ai", methods=["POST"])
def test_ai():
    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input="Movie Recap ဆိုတာဘာလဲ။ မြန်မာလိုတိုတိုရှင်းပြပါ။"
        )

        return jsonify({
            "status": "success",
            "result": response.output_text
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
