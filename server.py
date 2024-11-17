''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")

def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

   # Error checking - if text_to_analyze is empty, return None - From IBM STAFF recommendation - ritika
    if not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant_emotion from the response
    dominant_emotion = response['dominant_emotion']

    # Delete dominant_emotion from the dictionary so we can print the dict simply to get the customer's desired format
    del response['dominant_emotion']

    # If detector stat Ok - Return a formatted string scores and dominant emotion per customer request
    return "For the given statement, the system response is " + str(response) + " The dominant emotion is " + dominant_emotion
        

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
