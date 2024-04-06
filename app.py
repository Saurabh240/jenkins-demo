from flask import Flask
import requests

app = Flask(__name__)

app.secret_key = '67e3d7ab21c344e7abd58f84c59c8eb3'
app.config['SECRET_KEY'] = '67e3d7ab21c344e7abd58f84c59c8eb3'

@app.route("/")
def hello_world():
    response = requests.get('https://api.weatherbit.io/v2.0/current?&city=Raleigh&country=US&key=67e3d7ab21c344e7abd58f84c59c8eb3')
    if response.status_code == 200:
        data = response.json()
        sunrise_time = data['data'][0]['sunrise']
        return f"The sunrise time in Raleigh is: {sunrise_time}"
    else:
        return "Failed to retrieve data"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

