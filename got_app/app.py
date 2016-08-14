import sys
import logging

from flask import Flask

from got_app.lib.data_access import GOTDataset

log = logging.getLogger(__name__)
app = Flask(__name__)
data = GOTDataset()


@app.route('/')
def index():
    return 'Game Of Thrones Casualty Explorer'


@app.route('/data/battles')
def get_battles():
    return data.battles.to_json()


@app.route('/data/character_deaths')
def get_character_deaths():
    return data.character_deaths.to_json(orient='records')


@app.route('/data/locations')
def get_locations():
    return data.locations.to_json()


@app.route('/data/continents')
def get_continents():
    return data.continents.to_json()


def start_server():
    app.run(host='localhost', port=5000)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')
    start_server()
