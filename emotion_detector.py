try:
    from watson_nlp import EmotionClassifier
except ModuleNotFoundError:  # pragma: no cover
    EmotionClassifier = None


class EmotionDetector:
    def __init__(self):
        if EmotionClassifier is None:
            raise ModuleNotFoundError(
                "watson_nlp is not installed. Install dependencies from requirements.txt"
            )
        self.classifier = EmotionClassifier()


    def detect_emotion(self, text: str) -> str:

        """Detect emotions and return the formatted output as a string.


        Expected output format:
        - If no emotions: `No emotions detected.`
        - Otherwise: a multi-line string beginning with `Emotion Detection Results:`
        """
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty")

        result = self.classifier.run(text)
        emotions = result.get("emotion", {})

        if not emotions:
            return "No emotions detected."

        sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
        lines = ["Emotion Detection Results:", "-" * 30]
        for emotion, score in sorted_emotions:
            lines.append(f"{emotion.capitalize():15s}: {score:.4f}")
        return "\n".join(lines)

