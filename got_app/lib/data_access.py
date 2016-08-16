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
        self._continents = None
        self._locations = None
        self._political_regions = None

        self._populate()

    @property
    def locations(self):
        return self._get_dataframe_from_geojson(self._locations)

    @property
    def locations_json(self):
        return self._locations

    @property
    def continents(self):
        return self._get_dataframe_from_geojson(self._continents)

    @property
    def continents_json(self):
        return self._continents

    @property
    def political_regions(self):
        return self._get_dataframe_from_geojson(self._political_regions)

    @property
    def political_regions_json(self):
        return self._political_regions

    def _populate(self):
        self._populate_battle_data()
        self._populate_location_data()

    def _populate_battle_data(self):
        casualties_path = os.path.join(self.resources, 'battles')
        self.battles = self._get_dataframe_from_csv(os.path.join(casualties_path, 'battles.csv'))
        self.character_deaths = self._get_dataframe_from_csv(os.path.join(casualties_path, 'character-deaths.csv'))

    def _populate_location_data(self):
        geojson_path = os.path.join(self.resources, 'location', 'geojson')
        self._continents = self._get_json(os.path.join(geojson_path, 'continents.geojson'))
        self._locations = self._get_json(os.path.join(geojson_path, 'locations.geojson'))
        self._political_regions = self._get_json(os.path.join(geojson_path,
                                                             'political_regions.geojson'))

    def battles_with_locations(self):
        return self.battles.merge(self.locations, left_on='location', right_on='properties_name')

    def battles_by_continent(self):
        pass

    def battles_by_political_region(self):
        pass

    @classmethod
    def _get_json(cls, geojson_uri):
        with open(geojson_uri, 'r') as json_file:
            return json_file.read()

    @classmethod
    def _get_dataframe_from_csv(cls, csv_uri):
        return pd.DataFrame.from_csv(csv_uri)

    @classmethod
    def _get_dataframe_from_geojson(cls, json_str):
        geo_json = json.loads(json_str)
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
