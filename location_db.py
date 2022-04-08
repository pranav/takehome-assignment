import sys
from typing import Dict, Any

import logging
import requests
import json
import urllib.parse
from timezonefinder import TimezoneFinder


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
API_KEY = "**REDACTED**"
GEOCODE_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json"
DEFAULT_TIMEZONE = 'Etc/GMT-12'  # The least populated time zone in the world. consists of 2 islands in the pacific.
tzfinder = TimezoneFinder()


class LocationDb(object):
    def __init__(self):
        self.db_fp = open('locations.json', 'r+')
        self.location_to_timezone = json.load(self.db_fp)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_fp.close()

    def insert_location_timezone_into_db(self, location:str, timezone:str):
        self.location_to_timezone[location] = timezone
        self.db_fp.seek(0)
        json.dump(self.location_to_timezone, self.db_fp)

    def get_location_from_google_maps(self, location:str) -> str:
        """
        return time zone of given fuzzy location from google maps
        :param location: str
        """
        sanitized_location = urllib.parse.quote_plus(location)
        payload = {
            "address": sanitized_location,
            "key": API_KEY
        }
        result = requests.get(GEOCODE_ENDPOINT, params=payload)
        result.raise_for_status()
        locations = result.json()['results']
        if not locations:
            return DEFAULT_TIMEZONE
        lat_lon = result.json()['results'][0]['geometry']['location']
        return tzfinder.timezone_at(lng=lat_lon['lng'], lat=lat_lon['lat'])

    def get_location_timezone(self, location: str, use_google_maps=True) -> str:
        """
        Get timezone of given fuzzy location
        :param location: random string that could mean a location
        :param use_google_maps: if not found in database, fetch location from geocoding api. costs money. dont do.
        :return: something like "US/Eastern"
        """
        if location in self.location_to_timezone:
            return self.location_to_timezone[location]
        logging.debug(f"Location '{location}' not found in db, fetching from Google.")
        if use_google_maps:
            timezone = self.get_location_from_google_maps(location)
        else:
            return DEFAULT_TIMEZONE
        self.insert_location_timezone_into_db(location, timezone)
        return timezone