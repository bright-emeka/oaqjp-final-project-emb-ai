import pytest
from unittest.mock import patch

from emotion_detector import EmotionDetector

from emotion_formatter import format_emotion_output



class TestEmotionDetector:
    def setup_method(self):
        # Avoid requiring watson_nlp in the test environment
        with patch("emotion_detector.EmotionClassifier", create=True) as mock_classifier:
            mock_classifier.return_value = mock_classifier
            self.detector = EmotionDetector()


    def test_detect_emotion_returns_formatted_string(self):
        self.detector.classifier.run.return_value = {
            "emotion": {
                "joy": 0.8,
                "sadness": 0.1,
                "anger": 0.05,
                "fear": 0.03,
                "disgust": 0.02,
            }
        }
        result = self.detector.detect_emotion("I am very happy today!")
        assert isinstance(result, str)
        assert "Emotion Detection Results" in result
        assert "joy" in result.lower()


    def test_detect_emotion_empty_text_raises_error(self):
        with pytest.raises(ValueError):
            self.detector.detect_emotion("")

    def test_detect_emotion_whitespace_raises_error(self):
        with pytest.raises(ValueError):
            self.detector.detect_emotion("   ")


class TestEmotionFormatter:
    def test_format_emotion_output(self):
        emotions = {"joy": 0.8, "sadness": 0.1, "anger": 0.05}
        result = format_emotion_output(emotions)
        assert "Emotion Detection Results" in result
        assert "joy" in result.lower()

    def test_format_empty_emotions(self):
        result = format_emotion_output({})
        assert "No emotions detected" in result
