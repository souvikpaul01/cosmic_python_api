import requests
from flask import Flask, render_template

url = 'https://api.cosmicjs.com/v1/15833b00-e677-11ea-b521-4b536908cb9b/objects?'

headers= {'read_key':'SSL79aDN2ex9V2Bb0S2wOAwJG076H6OE2Yb9VNuTr58bdZNBXW',
          'pretty':'false',
          'hide_metafields' : 'true'}



response = requests.get(url, params=headers)
dict = response.json()

#print(dict['objects'])
#def get_data(): 
 #   for i in dict['objects']:
  #      x = i['slug']
   # return x
    #print(x)



app = Flask(__name__)

@app.route("/")

def main():
    return "Welcome to the Server"

@app.route("/index", methods = ['GET'])

def index():
    return render_template('home/ubuntu/index.html',title = dict)

#print(response.text.encode('utf8'))
#print(response.url)

if __name__ == "__main__":
    app.run(debug = True, host ="0.0.0.0", port = 3000)
