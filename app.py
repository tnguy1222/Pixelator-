"""Simple full-stack image generation app.

Backend: Flask. Generates images with OpenAI's DALL-E model
via the OpenAI REST API.
"""

import base64
import os

import requests
from flask import Flask, jsonify, request, send_from_directory

# Model: Defaults to dall-e-3
MODEL = os.environ.get("OPENAI_MODEL", "gpt-image-2")
API_KEY = os.environ.get("OPENAI_API_KEY", "")
API_URL = "https://api.openai.com/v1/images/generations"

app = Flask(__name__, static_folder="public", static_url_path="")


@app.route("/")
def index():
    return send_from_directory("public", "index.html")


@app.route("/api/generate", methods=["POST"])
def generate():
    if not API_KEY:
        return jsonify({"error": "OPENAI_API_KEY is not set on the server."}), 500

    data = request.get_json(silent=True) or {}
    user_prompt = (data.get("prompt") or "").strip()
    if not user_prompt:
        return jsonify({"error": "Please enter a description of the image."}), 400

    # Automatically enforce 16-bit style
    full_prompt = f"{user_prompt}, in 16-bit pixel art style, retro video game graphics"

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "n": 1,
        "size": "1024x1024",
    }

    try:
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload,
            timeout=120,
        )
    except requests.RequestException as exc:
        return jsonify({"error": f"Request to OpenAI failed: {exc}"}), 502

    if resp.status_code != 200:
        # Surface the API's error message when possible.
        try:
            msg = resp.json().get("error", {}).get("message", resp.text)
        except ValueError:
            msg = resp.text
        return jsonify({"error": f"OpenAI API error: {msg}"}), resp.status_code

    body = resp.json()
    image_data = _extract_image(body)
    if not image_data:
        return jsonify({"error": "No image was returned by the model."}), 502

    return jsonify({"image": image_data})


def _extract_image(body):
    """Pull the first image out of an OpenAI response (either b64 or url)."""
    for item in body.get("data", []):
        if item.get("b64_json"):
            return f"data:image/png;base64,{item['b64_json']}"
        elif item.get("url"):
            return item["url"]
    return None


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=True)
