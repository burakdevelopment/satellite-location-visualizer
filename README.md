# Satellite Location Visualizer

Satellite location visualizer is a Python-based application that visualizes the real-time location of various satellites orbiting Earth. It utilizes satellite tracking data and displays their positions on a world map using the `matplotlib` and `basemap` libraries.

## Key Features & Benefits

- **Real-time Satellite Tracking:** Fetches and displays the current location of various satellites.
- **Interactive Visualization:** Uses `matplotlib` and `basemap` to plot satellite positions on a world map.
- **Satellite Selection:** Allows users to select from a predefined list of satellites to track.
- **Animation:** Provides an animated visualization of satellite movement over time.
- **User-Friendly Interface:** Features a simple Tkinter-based GUI for easy interaction.

## Prerequisites & Dependencies

Before running the satellite location visualizer, ensure you have the following dependencies installed:

- Python 3.x
- `requests`
- `matplotlib`
- `basemap` (mpl_toolkits)
- `tkinter` (for GUI)
- `ttk` (for enhanced Tkinter widgets)

You can install these dependencies using pip:

```bash
pip install requests matplotlib basemap
```

## Installation & Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/burakdevelopment/satellite-location-visualizer.git
   cd satellite-location-visualizer
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt # (if a requirements.txt file exists, otherwise see dependencies section)
   ```

3. **Obtain an API Key:**

   - This project requires an API key to fetch satellite data. You'll need to register for an API key from a satellite tracking service (e.g., N2YO, Space-Track).  Replace `"yourapikey:D"` in the `satellitesimulation (Copy).py` file with your actual API key. (from here: http://n2yo.com/api/)

4. **Run the application:**

   ```bash
   python satellitesimulation (Copy).py
   ```

## Usage Examples & API Documentation

The main script `satellitesimulation (Copy).py` contains the core logic for fetching satellite data and visualizing their locations.

**Example Usage:**

1.  Open the `satellitesimulation (Copy).py` file.
2.  Locate the `satellites` dictionary:

```python
satellites = {
    "ISS": 25544,
    "Hubble Uzay Teleskobu": 20580,
    "Tiangong Uzay İstasyonu": 48274,
    "NOAA-20": 43013,
    "GOES-16": 41753,
    "Starlink 44942": 44942,
    "GPS PRN 01": 24876,
    "Envisat": 27386
}
```

This dictionary maps satellite names to their NORAD IDs. You can add or modify entries to track different satellites.

3.  Run the script to start the visualization. The Tkinter GUI will display a dropdown menu to select a satellite and a map showing its location.

## Configuration Options

- **API Key:** The `API_KEY` variable in `satellitesimulation (Copy).py` must be set to a valid API key for fetching satellite data. (from here: http://n2yo.com/api/)
- **Satellites:** The `satellites` dictionary can be modified to include the NORAD IDs of the satellites you wish to track.
- **Visualization Parameters:** You can adjust parameters like the map projection, animation speed, and marker styles in the code to customize the visualization.

## Contributing Guidelines

We welcome contributions to the satellite location visualizer project! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Submit a pull request to the main branch.

Please ensure your code adheres to the project's coding style and includes appropriate documentation and tests.

## License Information

This project is licensed under the MIT License. See the `LICENSE` file for details.

```
MIT License

Copyright (c) 2024 burakdevelopment

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

## Acknowledgments

This project utilizes the following third-party resources:

- `requests` library for making HTTP requests.
- `matplotlib` and `basemap` libraries for data visualization.
- Satellite tracking data from [specify the data source, e.g., N2YO].
