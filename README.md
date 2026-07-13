# Emotion Detection Application

An emotion detection web application built with Flask and IBM Watson NLP.

## Project Structure

```
oaqjp-final-project-emb-ai/
├── app.py                 # Flask web application
├── emotion_detector.py    # Watson NLP emotion detection logic
├── emotion_formatter.py   # Output formatting utilities
├── requirements.txt       # Python dependencies
├── setup.py               # Package configuration
├── tests/
│   ├── __init__.py
│   └── test_emotion_detector.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## Running Tests

```bash
pytest tests/ -v
```

## Static Code Analysis

```bash
pylint app.py emotion_detector.py emotion_formatter.py
flake8 app.py emotion_detector.py emotion_formatter.py
```
