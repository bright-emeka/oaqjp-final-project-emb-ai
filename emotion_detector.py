from watson_nlp import EmotionClassifier


class EmotionDetector:
    def __init__(self):
        self.classifier = EmotionClassifier()

    def detect_emotion(self, text):
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty")
        result = self.classifier.run(text)
        emotions = result.get("emotion", {})
        return emotions
