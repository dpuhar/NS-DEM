# NS-DEM 
This script utilizes the SentinelSat and Elevation libraries in Python to search for Sentinel-2 satellite products, download the data, and process a Digital Elevation Model (DEM) with a 10-meter resolution.

Prerequisites

    Python 3.6 or higher
    Installation of the following libraries:
        SentinelSat
        elevation

Setup

    Clone the repository or download the script directly.
    Ensure that you have a valid Copernicus Open Access Hub account to access Sentinel-2 data.
    Update the script with your Copernicus Open Access Hub credentials.
    Make sure the necessary GeoJSON files and input parameters are correctly set.

Usage

    Run the script in a Python environment with the required libraries installed.
    Check the specified file paths for GeoJSON input and output data to ensure proper execution.
    The script will automatically download the Sentinel-2 data based on the defined parameters.
    It will also process a Digital Elevation Model (DEM) with a 10-meter resolution for the specified geographic bounds.

Notes

    Verify that the specified geographic bounds for the DEM processing are accurate.
    After this, you will be able to get slope and curvature data from DEM.
