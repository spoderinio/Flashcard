import json
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Пример за зареждане на данни от JSON файл
def load_words():
    with open('norwegian_words.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Зареждане на words при стартиране на приложението
words = load_words()

@app.route('/')
def index():
    # Проверка дали words съдържа данни
    current_word = words[0] if words else {}
    return render_template('index.html', words=json.dumps(words), current_word=current_word)

@app.route('/api/words')
def get_words():
    return jsonify(words)

if __name__ == '__main__':
    app.run(debug=True)