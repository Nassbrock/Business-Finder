# Business Finder

Business Finder is a Streamlit application that helps users find businesses in a specified area using Google Maps. The application allows users to search for businesses, view search history, and download search results as CSV files.

## Features

- **Interactive Map**: Select the area for searching businesses using an interactive map.
- **Filters**: Apply various filters to narrow down the search results.
- **Search History**: View the history of past searches in the sidebar.
- **CSV Download**: Download the search results as CSV files directly from the application.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/business-finder.git
    cd business-finder
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Google Maps API key:

    Create a `.env` file in the root directory of the project and add your Google Maps API key:

    ```env
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key
    ```

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

## Project Structure

business-finder/
├── components/
│ ├── filters.py
│ ├── map.py
│ ├── results.py
│ └── search.py
├── utils/
│ └── google_maps.py
├── app.py
├── requirements.txt
└── README.md

markdown
Copy code

- **components/**: Contains the components used in the application (filters, map, results, search).
- **utils/**: Contains utility scripts (Google Maps client).
- **app.py**: Main application script.
- **requirements.txt**: List of dependencies.
- **README.md**: Project documentation.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes.
4. Commit your changes with a clear message.
5. Push to your branch.
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Maps API](https://developers.google.com/maps)
