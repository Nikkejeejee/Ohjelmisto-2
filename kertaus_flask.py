from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def sano_moi():
    return "No terve terve"


@app.route('/tervehdys')
def terve():
    return "Moi"

# wtf does this do??
@app.route('/summa')
def summafunktio():
    argumentit = request.args
    num1 = argumentit.get('num1')
    num2 = argumentit.get('num2')
    print(num2)
    print(argumentit)
    summa = num1 + num2
    return summa


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
