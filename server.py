from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emo_detector():

    '''
        This code gets text from an HTML interface and 
        runs emotion detection on it, using the emotion_detector()
        function. The output returns different emotions followed by a score..
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    return response

@app.route("/")
def render_first_page():
    '''
        This code renders the fist page of the application
    '''
    return render_template("index.html")

if __name__== "__main__":
    ''' 
        This code executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)