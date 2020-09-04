import requests
from flask import Flask, render_template
import json
url_api = 'https://api.cosmicjs.com/v1/15833b00-e677-11ea-b521-4b536908cb9b/objects?'

params= {'read_key':'SSL79aDN2ex9V2Bb0S2wOAwJG076H6OE2Yb9VNuTr58bdZNBXW',
          'pretty':'false',
          'hide_metafields' : 'true'}

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def index():
    response = requests.get(url_api, params=params)
    json_response = response.json()
    posts = json_response['objects']

    return render_template('index.html',posts = posts, l = len(posts) )


if __name__ == "__main__":
    app.run(debug = True, host ="0.0.0.0", port = 3000)

