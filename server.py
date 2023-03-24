from flask import Flask, request, jsonify
from language_translator.translator import englishToFrench

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data['text']
    translation = englishToFrench(text)
    return jsonify({'translation': translation})
