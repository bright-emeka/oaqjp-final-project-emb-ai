from flask import Flask, render_template, request, jsonify
from emotion_detector import EmotionDetector
from emotion_formatter import format_emotion_output


app = Flask(__name__)
detector = EmotionDetector()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector():
    text = request.args.get("textToAnalyze", "").strip()
    try:
        emotions = detector.detect_emotion(text)
        formatted = format_emotion_output(emotions)
        return f"<pre>{formatted}</pre>"
    except ValueError as e:
        return f"<pre style='color: red;'>Error: {e}</pre>"
    except Exception as e:
        return f"<pre style='color: red;'>Unexpected error: {e}</pre>"


@app.route("/api/emotion", methods=["POST"])
def api_emotion():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()
    try:
        emotions = detector.detect_emotion(text)
        return jsonify({"text": text, "emotions": emotions})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
