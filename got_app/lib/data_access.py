import os
import json

import got_app
import pandas as pd


class GOTDataset(object):
    def __init__(self):
        self.app_root = os.path.join(os.path.dirname(got_app.__file__), os.path.pardir)
        self.resources = os.path.join(self.app_root, 'resources')

    @property
    def battles(self):
        path = os.path.join(self.resources, 'casualties', 'battles.csv')
        return self._get_dataframe_from_csv(path)

    @property
    def character_deaths(self):
        path = os.path.join(self.resources, 'casualties', 'character-deaths.csv')
        return self._get_dataframe_from_csv(path)

    @property
    def continents(self):
        path = os.path.join(self.resources, 'location', 'geojson', 'continents.geojson')
        return self._get_dataframe_from_geojson(path)

    @property
    def locations(self):
        path = os.path.join(self.resources, 'location', 'geojson', 'locations.geojson')
        return self._get_dataframe_from_geojson(path)

    @classmethod
    def _get_dataframe_from_csv(cls, csv_uri):
        return pd.DataFrame.from_csv(csv_uri)

    @classmethod
    def _get_dataframe_from_geojson(cls, geojson_uri):
        with open(geojson_uri, 'r') as json_file:
            geo_json = json.load(json_file)
        return pd.DataFrame.from_records(geo_json['features'])
