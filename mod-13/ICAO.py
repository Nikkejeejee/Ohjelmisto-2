import mysql.connector
from flask import Flask, jsonify

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='sunmuts1s',
    autocommit=True
)

app = Flask(__name__)

airportDatabase = {
    "EFHK": {
        "Name": "Helsinki Vantaa Airport",
        "Municipality": "Helsinki"
    }
}


@app.route('/airport/<icao>')
def get_airport_info(icao):
    if icao in airportDatabase:
        airport_info = airportDatabase[icao]
        return jsonify({"ICAO": icao, "Name": airport_info["Name"], "Municipality": airport_info["Municipality"]})
    else:
        return jsonify({"error": "Lentokenttää ei löydy"}, 404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
