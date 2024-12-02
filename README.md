Flask Emotion Detection Application##

This is a Flask-based web application for detecting emotions in text using the Watson NLP Emotion Detection API. Users can input text and receive an analysis of the emotions associated with it, along with the dominant emotion.

Features

Accepts a text statement via a POST request.

Detects emotions such as anger, disgust, fear, joy, and sadness.

Returns the emotion scores and the dominant emotion in the text.

Includes error handling for blank inputs, invalid JSON payloads, and type errors.

Provides meaningful responses for invalid or missing data.
