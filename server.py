from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    data = request.json
    text_to_analyze = data.get("text", "")

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text_to_analyze)

    response_message = (f"For the given statement, the system response is "
                        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")

    return jsonify({"analysis": result, "message": response_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)