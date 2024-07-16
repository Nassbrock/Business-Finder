import streamlit as st
import folium
from streamlit_folium import st_folium
import os
from dotenv import load_dotenv
from folium.plugins import Draw

load_dotenv()  # Load environment variables from .env file

class Map:
    def __init__(self):
        self.map_location = [42.6977, 23.3219]  # Default location (Sofia, Bulgaria)
        self.radius = 5000  # Default radius in meters

    def display(self):
        st.text("Use the map below to select the area for searching businesses.")
        m = folium.Map(location=self.map_location, zoom_start=13)

        # Enable drawing and editing features
        draw = Draw(
            export=True,
            draw_options={
                'polyline': False,
                'polygon': False,
                'rectangle': False,
                'marker': False,
                'circle': True,
                'circlemarker': False
            }
        )
        draw.add_to(m)

        st_data = st_folium(m, width=900, height=600)  # Increased size

        if st_data and 'last_active_drawing' in st_data and st_data['last_active_drawing']:
            drawing = st_data['last_active_drawing']
            if drawing['geometry']['type'] == 'Point' and 'properties' in drawing:
                self.map_location = [
                    drawing['geometry']['coordinates'][1],  # latitude
                    drawing['geometry']['coordinates'][0]   # longitude
                ]
                self.radius = drawing['properties'].get('radius', self.radius)

        return self.map_location, self.radius
