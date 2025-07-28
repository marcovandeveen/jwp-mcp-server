from flask import Flask, jsonify, send_file, request
import requests
import os

app = Flask(__name__)

JWP_API_BASE = "https://api.jwplayer.com/v2"
JWP_API_KEY = os.getenv("JWP_API_KEY")

@app.route('/.well-known/ai-plugin.json')
def plugin_manifest():
    return send_file(".well-known/ai-plugin.json")

@app.route('/openapi.yaml')
def openapi_spec():
    return send_file("openapi.yaml")

@app.route('/media/<media_id>')
def get_media(media_id):
    headers = {
        "Authorization": f"Bearer {JWP_API_KEY}"
    }
    response = requests.get(f"{JWP_API_BASE}/media/{media_id}", headers=headers)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000))) 