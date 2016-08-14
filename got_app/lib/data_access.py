import os
import json

import got_app
import pandas as pd


class GOTDataset(object):
    def __init__(self):
        self.app_root = os.path.join(os.path.dirname(got_app.__file__), os.path.pardir)
        self.resources = os.path.join(self.app_root, 'resources')

        self.battles = None
        self.character_deaths = None
        self.continents = None
        self.locations = None
        self.political_regions = None

        self._populate()

    def _populate(self):
        self._populate_battle_data()
        self._populate_location_data()

    def _populate_battle_data(self):
        casualties_path = os.path.join(self.resources, 'battles')
        self.battles = self._get_dataframe_from_csv(os.path.join(casualties_path, 'battles.csv'))
        self.character_deaths = self._get_dataframe_from_csv(os.path.join(casualties_path, 'character-deaths.csv'))

    def _populate_location_data(self):
        geojson_path = os.path.join(self.resources, 'location', 'geojson')
        self.continents = self._get_dataframe_from_geojson(os.path.join(geojson_path, 'continents.geojson'))
        self.locations = self._get_dataframe_from_geojson(os.path.join(geojson_path, 'locations.geojson'))
        self.political_regions = self._get_dataframe_from_geojson(os.path.join(geojson_path,
                                                                               'political_regions.geojson'))

    def battles_with_locations(self):
        return self.battles.merge(self.locations, left_on='location', right_on='properties_name')

    def battles_by_continent(self):
        pass

    def battles_by_political_region(self):
        pass

    @classmethod
    def _get_dataframe_from_csv(cls, csv_uri):
        return pd.DataFrame.from_csv(csv_uri)

    @classmethod
    def _get_dataframe_from_geojson(cls, geojson_uri):
        with open(geojson_uri, 'r') as json_file:
            geo_json = json.load(json_file)

        flat_geo_json = list()
        for entry in geo_json['features']:
            flat_entry = dict()
            for key, value in entry.items():
                if isinstance(value, dict):
                    for subkey, subvalue in value.items():
                        flat_entry['{0}_{1}'.format(key, subkey)] = subvalue
                else:
                    flat_entry[key] = value
            flat_geo_json.append(flat_entry)

        return pd.DataFrame.from_records(flat_geo_json)
