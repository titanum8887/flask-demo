from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="color: purple">Привіт я працюю Flask та Docker'


if __name__== '__main__':
    app.run(host='0.0.0.0', port=80)
