from emotion_detector import EmotionDetector


def format_emotion_output(emotions):
    if not emotions:
        return "No emotions detected."

    sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
    lines = ["Emotion Detection Results:", "-" * 30]
    for emotion, score in sorted_emotions:
        lines.append(f"{emotion.capitalize():15s}: {score:.4f}")
    return "\n".join(lines)
