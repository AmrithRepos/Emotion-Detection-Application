"""
Flask application for emotion detection.
"""
from flask import Flask, request, jsonify
from emotion_detection import emotion_detector  # Import the defined function

app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Flask route for emotion detection.
    """
    try:
        input_data = request.get_json()
        if not input_data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        statement = input_data.get('statement', '')
        if not statement.strip():  # Checks for blank input from the user
            return jsonify({"response": "Invalid text! Please try again!"}), 400

        result = emotion_detector(statement)

        if result.get('dominant_emotion') is None:  # Handles the invalid emotion detection
            return jsonify({"response": "Invalid text! Please try again!"}), 400

        response_message = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({"response": response_message}), 200

    except KeyError as key_error:
        return jsonify({"error": f"Missing key: {str(key_error)}"}), 400
    except ValueError as value_error:
        return jsonify({"error": f"Invalid value: {str(value_error)}"}), 400
    except TypeError as type_error:
        return jsonify({"error": f"Type error: {str(type_error)}"}), 400


if __name__ == '__main__':
    app.run(debug=True)
