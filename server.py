from __future__ import annotations

import sys

from flask import Flask, jsonify, render_template, request

from emotion_detector import EmotionDetector


app = Flask(__name__)

detector = EmotionDetector()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_page():
    text = request.args.get("textToAnalyze", "").strip()
    try:
        formatted = detector.detect_emotion(text)
        return f"<pre>{formatted}</pre>", 200
    except ValueError as e:
        # blank/invalid input -> 400
        return f"<pre style='color: red;'>Error: {e}</pre>", 400
    except Exception as e:  # pragma: no cover
        return f"<pre style='color: red;'>Unexpected error: {e}</pre>", 500



@app.route("/api/emotion", methods=["POST"])
def api_emotion():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    try:
        formatted = detector.detect_emotion(text)
        return jsonify({"text": text, "result": formatted})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:  # pragma: no cover
        return jsonify({"error": f"Unexpected error: {e}"}), 500


def run_static_analysis() -> int:
    """Run static analysis tools and return their combined exit code."""
    import subprocess

    cmds = [
        [sys.executable, "-m", "pylint", "server.py"],
        [sys.executable, "-m", "flake8", "server.py"],
    ]

    exit_code = 0
    for cmd in cmds:
        proc = subprocess.run(cmd, capture_output=False)
        exit_code = max(exit_code, proc.returncode)

    return exit_code


if __name__ == "__main__":
    if "--static-analysis" in sys.argv:
        sys.exit(run_static_analysis())

    app.run(debug=True, host="0.0.0.0", port=5000)

