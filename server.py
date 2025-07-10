"""
Flask web server for Emotion Detection application using Watson NLP by Hemant, K.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page with the emotion detection form."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze the input text and return the emotion scores and dominant emotion.
    Displays an error message if input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    # Handle invalid or empty input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    formatted = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return formatted

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
