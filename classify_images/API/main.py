
import os
import json
from flask import Flask, request
from process_image import classify_images

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    envelope = request.get_json()
    
    if not envelope:
        msg = "no message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "image_paths" not in envelope:
        msg = "invalid request format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    image_paths = envelope["image_paths"]

    if isinstance(image_paths, list):

        # call classify_images to process list of images
        response = classify_images(image_paths)

        return (response, 200)
    else:
        msg = "invalid request format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400


if __name__ == '__main__':
    """Run a Flask Server at localhost:8050"""
    app.run(host="0.0.0.0", port=8050)