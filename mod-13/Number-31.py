from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime_number(number):
    is_prime_result = is_prime(number)
    response_data = {
        "Number": number,
        "isPrime": is_prime_result
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)