import requests
import json

def emotion_detector(text_to_analyze):

     
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Error checking - Online Forums - From IBM STAFF recommendation - ritika
    if response.status_code != 200:
        return None
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extracting the dominant emotion and score from the response
    max_emotion, max_value = max(emotions.items(), key=lambda t: t[1])
    # Add a key:value pair for the dominant emotion to the emotions dict
    emotions['dominant_emotion'] = max_emotion

    # Returning a dictionary containing emotion sentiment results
    return emotions
