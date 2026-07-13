import emotion_detector

class DummyClassifier:
    def run(self, text):
        return {'emotion': {'joy': 0.8, 'sadness': 0.1, 'anger': 0.05}}

emotion_detector.EmotionClassifier = DummyClassifier
detector = emotion_detector.EmotionDetector()
print(detector.detect_emotion('I am very happy today!'))
