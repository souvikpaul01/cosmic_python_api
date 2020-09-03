import requests
from flask import Flask, render_template
import json
url = 'https://api.cosmicjs.com/v1/15833b00-e677-11ea-b521-4b536908cb9b/objects?'

headers= {'read_key':'SSL79aDN2ex9V2Bb0S2wOAwJG076H6OE2Yb9VNuTr58bdZNBXW',
          'pretty':'false',
          'hide_metafields' : 'true'}



response = requests.get(url, params=headers)

json_response = response.json()

#dict = json.loads(json_response)

j_dict = json_response['objects']
'''
for objects in j_dict:
    title = objects['title']
    url = objects['metadata']['hero']['imgix_url']
         #   return title,images
'''

title = []
url = []

app = Flask(__name__)

@app.route("/")

def main():
    return "Welcome to the Server"

@app.route("/index", methods = ['GET'])

def index():
    for objects in j_dict:
        title.append(objects['title'])
        url.append(objects['metadata']['hero']['imgix_url'])
    
    return render_template('index.html',title = title, url = url, l = len(j_dict))


if __name__ == "__main__":
    app.run(debug = True, host ="0.0.0.0", port = 3000)

