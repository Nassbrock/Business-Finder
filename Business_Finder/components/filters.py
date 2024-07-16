import streamlit as st

class Filters:
    def __init__(self):
        self.filters = {}

    def display(self):
        st.sidebar.header("Step 2: Apply Filters")

        business_types = ["store", "restaurant", "plumber", "electrician", "cafe", "salon"]
        selected_business_types = st.sidebar.multiselect("Business Types", business_types, default=business_types)

        st.sidebar.markdown("**Additional Filters**")
        self.filters = {
            "Without websites": st.sidebar.checkbox("Without websites", value=True),
            "Operational": st.sidebar.checkbox("Operational", value=True),
            "Has Phone Number": st.sidebar.checkbox("Has Phone Number", value=False),
            "Has Recent Reviews": st.sidebar.checkbox("Has Recent Reviews", value=False),
            "Has Any Reviews": st.sidebar.checkbox("Has Any Reviews", value=False),
            "Business Types": selected_business_types,
            "All Businesses": st.sidebar.checkbox("Get all businesses in the area", value=False)
        }
        return self.filters
