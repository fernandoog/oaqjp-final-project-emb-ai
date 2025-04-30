"""
Flask server for the Emotion Detection API
"""

from flask import Flask, request, jsonify
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Processes input text and returns detected emotions.
    """
    data = request.json
    text_to_analyze = data.get("text", "").strip()

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"analysis": result, "message": response_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)