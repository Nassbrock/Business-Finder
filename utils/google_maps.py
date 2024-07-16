import googlemaps
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class GoogleMapsClient:
    def __init__(self):
        api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        if not api_key:
            raise ValueError("No API key found. Please set the GOOGLE_MAPS_API_KEY environment variable.")
        print(f"Using API Key: {api_key}")  # Debug print to check the API key
        self.client = googlemaps.Client(key=api_key)

    def search_businesses(self, location, radius, business_type):
        try:
            places_result = self.client.places_nearby(location=location, radius=radius, type=business_type)
            print(f"Places Result: {places_result}")  # Debug print for places result
            return places_result
        except googlemaps.exceptions.ApiError as e:
            print(f"Google Maps API error: {e}")
            return None

    def has_website(self, place_id):
        try:
            place_details = self.client.place(place_id=place_id)
            print(f"Place Details: {place_details}")  # Debug print for place details
            return 'website' in place_details['result']
        except googlemaps.exceptions.ApiError as e:
            print(f"Google Maps API error: {e}")
            return False

    def find_businesses(self, location, radius, business_types, only_without_websites=True):
        businesses_list = []
        for business_type in business_types:
            businesses = self.search_businesses(location, radius, business_type)
            if businesses:
                for business in businesses['results']:
                    has_website = self.has_website(business['place_id'])
                    if not only_without_websites or (only_without_websites and not has_website):
                        businesses_list.append({
                            'name': business['name'],
                            'address': business['vicinity'],
                            'place_id': business['place_id'],
                            'type': business_type,
                            'maps_url': f"https://www.google.com/maps/search/?api=1&query={business['geometry']['location']['lat']},{business['geometry']['location']['lng']}",
                            'gbp_profile': f"https://www.google.com/maps/place/?q=place_id:{business['place_id']}",
                            'has_website': has_website
                        })
        return businesses_list
