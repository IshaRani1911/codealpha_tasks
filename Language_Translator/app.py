from flask import Flask, render_template, request, send_file
from deep_translator import GoogleTranslator
from gtts import gTTS

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", result="",text="",source="",target="")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["inputText"]
    source = request.form.get("sourceLanguage", "")
    target = request.form.get("targetLanguage", "")
    if text.strip() == "":
        return render_template("index.html",text=text,source=source,target=target,result="Please enter some text.")
    if source == "":
        return render_template("index.html",text=text,source=source,target=target,result="Please select a source language.")
    if target == "":
        return render_template("index.html",text=text,source=source,target=target,result="Please select a target language.")
    if source == target:
        return render_template("index.html",text=text, source=source,target=target,result="Please select different source and target languages.")
    translator = GoogleTranslator(
        source=source,
        target = target
    )
    translated_text = translator.translate(text)
    return render_template("index.html",text=text, source=source, target= target ,result=translated_text)

@app.route("/speak", methods=["POST"])
def speak():

    data = request.get_json()

    text = data["text"]
    target = data["target"]

    tts = gTTS(text=text, lang=target)

    tts.save("speech.mp3")

    return send_file(
        "speech.mp3",
        mimetype="audio/mpeg"
    )

if __name__ == "__main__":
    app.run(debug=True)