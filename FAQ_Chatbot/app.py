from flask import Flask, render_template, request, jsonify
from matcher import FAQMatcher

app = Flask(__name__)
matcher = FAQMatcher()  # Loaded once when server starts

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    response = matcher.get_best_match(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)