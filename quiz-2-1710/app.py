from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/people/"

def get_character_data(character_id):
    response = requests.get(f"{SWAPI_BASE_URL}{character_id}/")
    return response.json()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/character', methods=['GET'])
def character():
    character_id = request.args.get('id')
    character_data = get_character_data(character_id)
    return render_template('character-templates.html', character=character_data)
   

if __name__ == '__main__':
    app.run(debug=True)
