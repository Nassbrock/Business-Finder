import streamlit as st
import pandas as pd

class Results:
    def __init__(self):
        self.businesses = []

    def display(self, businesses):
        self.businesses = businesses
        df = pd.DataFrame(self.businesses)
        st.write("### Businesses Found")
        st.dataframe(df)

        st.write("### Detailed View")
        for index, business in df.iterrows():
            with st.expander(business["name"]):
                st.write(f"**Address:** {business['address']}")
                st.write(f"**Google Maps URL:** [Open in Google Maps]({business['maps_url']})")
                st.write(f"**Google Business Profile:** [View GBP]({business['gbp_profile']})")
                st.write(f"**Business Type:** {business['type']}")
                st.write(f"**Has Website:** {'Yes' if business['has_website'] else 'No'}")
