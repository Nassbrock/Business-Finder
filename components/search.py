import streamlit as st
from utils.google_maps import GoogleMapsClient

class Search:
    def __init__(self):
        self.gmaps_client = GoogleMapsClient()
        self.businesses = []

    def perform_search(self, map_location, radius, filters):
        only_without_websites = not filters["All Businesses"]
        self.businesses = self.gmaps_client.find_businesses(map_location, radius, filters['Business Types'], only_without_websites)
        return self.businesses
