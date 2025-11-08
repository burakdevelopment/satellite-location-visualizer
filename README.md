# Satellite Location Visualizer

Satellite Orbit Visualizer is a Python-based application that calculates and visualizes the ground tracks of satellites in Earth orbit.

Instead of relying on a third-party API for location data, this project uses the SGP4 orbital propagation model to calculate satellite positions in real time. It pulls the latest Two-Line Element (TLE) orbital data from CelesTrak and uses the skyfield library to estimate the satellite's current latitude/longitude position with scientific accuracy.

The calculated orbital path is plotted on a world map using matplotlib and basemap.

## Key Features

- Real-Time SGP4 Calculation: Calculates satellite positions instantly using the SGP4 model, rather than retrieving them from an API.

- TLE Data Integration: Retrieves orbital parameters (TLE) directly from CelesTrak.

- No API Key Required: No external API key is required for position data. Only an internet connection is required to download TLE data.

- Multi-Satellite Tracking: Allows multiple satellites to be selected and tracked simultaneously with a simple tkinter-based interface.

- Animated Ground Track: Visualizes satellite orbital paths with a real-time animation.

- 2D World Map: Displays the current location and path of satellites on a world map using matplotlib and basemap.

## Prerequisites & Dependencies

Before running the satellite location visualizer, ensure you have the following dependencies installed:

- Python 3.x
- `requests`
- `matplotlib`
- `basemap` (mpl_toolkits)
- `skyfield` (for SGP4 orbit calculations)
- `tkinter` (for GUI)

You can install these dependencies using pip:

```bash
pip install requests matplotlib basemap skyfield
```

## Installation & Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/burakdevelopment/satellite-location-visualizer.git
   cd satellite-location-visualizer
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt 
   ```

4. **Run the application:**

   ```bash
   python satellitesimulation.py
   ```

## Usage Examples


**Example Usage:**

1.  Open the `satellitesimulation.py` file.
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

