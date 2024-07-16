import streamlit as st
from components.map import Map
from components.filters import Filters
from components.results import Results
from components.search import Search
import pandas as pd

st.set_page_config(page_title="Business Finder", layout="wide")

# CSS to style the buttons and adjust their positions
st.markdown("""
    <style>
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .search-button {
            padding: 0.75rem 2rem;
            font-size: 1rem;
            background-color: #ff4b4b;
            color: white;
            border: none;
            border-radius: 0.25rem;
            cursor: pointer;
        }
        .button-container {
            display: flex;
            justify-content: flex-end;
            align-items: center;
        }
        .csv-button {
            padding: 0.5rem 1rem;
            margin-left: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header with Search button
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("""
    <div class="header-container">
        <h1>Business Finder</h1>
    </div>
    """, unsafe_allow_html=True)
with col2:
    search_button = st.button("Search", key="search_button")

# Initialize components
map_component = Map()
filters_component = Filters()
results_component = Results()
search_component = Search()

# Display filters in the sidebar
selected_filters = filters_component.display()

# Initialize session state for storing search results and history
if "businesses" not in st.session_state:
    st.session_state.businesses = []
if "search_history" not in st.session_state:
    st.session_state.search_history = []

# Display the map and results side by side
col1, col2 = st.columns([3, 2])
with col1:
    st.subheader("Select Area")
    map_location, radius = map_component.display()

if search_button:
    results = search_component.perform_search(map_location, radius, selected_filters)
    st.session_state.businesses = results
    st.session_state.search_history.append({
        "location": map_location,
        "radius": radius,
        "filters": selected_filters,
        "results": results
    })

# Display search history in the sidebar
st.sidebar.header("Search History")
for i, search in enumerate(st.session_state.search_history):
    with st.sidebar.expander(f"Search {i+1}"):
        st.write(f"Location: {search['location']}")
        st.write(f"Radius: {search['radius']} meters")
        st.write(f"Filters: {search['filters']}")
        st.write(f"Results: {len(search['results'])} businesses found")
        df = pd.DataFrame(search['results'])
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download this search as CSV",
            data=csv,
            file_name=f'search_{i+1}_results.csv',
            mime='text/csv',
            key=f"download_button_{i}"
        )

with col2:
    if st.session_state.businesses:
        # Display header and download button on the same level
        col2.subheader("Search Results")
        df = pd.DataFrame(st.session_state.businesses)
        
        # Container for the "Download CSV" button
        col3, col4 = col2.columns([4, 1])
        with col4:
            st.download_button(
                label="Download results as CSV",
                data=df.to_csv(index=False),
                file_name='business_finder_results.csv',
                mime='text/csv',
                key="download_button"
            )
        
        results_component.display(st.session_state.businesses)
