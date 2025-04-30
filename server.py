import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if text is empty or just spaces
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code == 200:
        emotions_data = response.json()
        emotions = emotions_data.get("emotion_predictions", [{}])[0].get("emotion", {})
        relevant_emotions = {key: emotions.get(key, 0) for key in ["anger", "disgust", "fear", "joy", "sadness"]}
        dominant_emotion = max(relevant_emotions, key=relevant_emotions.get)
        relevant_emotions["dominant_emotion"] = dominant_emotion
        return relevant_emotions

    return {"error": f"Request failed with status code {response.status_code}"}