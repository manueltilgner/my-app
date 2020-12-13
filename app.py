from flask import Flask
import os

NAME = os.environ.get('NAME', 'Teilnehmer')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return 'Data Engineer Schulung: Herzlich Willkommen {}!'.format(NAME)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(5000))
