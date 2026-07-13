import pytest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector:
    def test_empty_text_returns_none_values(self):
        result = emotion_detector("   ")
        assert result["dominant_emotion"] is None
        assert result["anger"] is None
        assert result["sadness"] is None

    def test_400_status_returns_none_values(self, monkeypatch):
        class MockResponse:
            status_code = 400

            def json(self):
                return {}

        def mock_post(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr("EmotionDetection.emotion_detection.requests.post", mock_post)
        result = emotion_detector("hello")
        assert result["dominant_emotion"] is None
        assert set(result.keys()) == {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"}
        assert all(value is None for value in result.values())

    def test_successful_response_returns_dominant_emotion(self, monkeypatch):
        class MockResponse:
            status_code = 200

            def json(self):
                return {
                    "emotion": {
                        "document": {
                            "emotion": {
                                "anger": 0.1,
                                "disgust": 0.2,
                                "fear": 0.3,
                                "joy": 0.4,
                                "sadness": 0.5,
                            }
                        }
                    }
                }

        monkeypatch.setattr("EmotionDetection.emotion_detection.requests.post", lambda *args, **kwargs: MockResponse())
        result = emotion_detector("I am happy")
        assert result["dominant_emotion"] == "sadness"
        assert result["joy"] == 0.4
        assert result["sadness"] == 0.5
