# Weather-Visualizer-with-Error-Handling
“This Python project loads weather data from a CSV file, processes it using NumPy, and visualizes temperature trends with Matplotlib. A Tkinter GUI allows users to select a city and view graphs along with average, maximum, and minimum temperature values.”


# Weather Data Visualizer

A simple Python application that reads weather data from a CSV file and visualizes temperature trends for different cities using Tkinter (GUI), NumPy, and Matplotlib.

## Features
- Load data from `weatherr.csv`
- Select city from dropdown
- Show Average, Maximum, Minimum temperature
- Plot temperature vs. day
- Handles errors (missing file, invalid CSV, wrong values)

## CSV Format

City,Day,Temperature
Delhi,1,25.3
Delhi,2,26.1
Mumbai,1,29.0


## Requirements
pip install numpy matplotlib


## How to Run
1. Place `weatherr.csv` next to the script  
2. Run:
python weather_visualizer.py
3. Choose a city → Click **Show Temperature Graph**

## Output
- Temperature summary inside GUI  
- Line graph displayed using Matplotlib  

## Notes
- Works even if some CSV rows are invalid  
- Shows messagebox errors instead of crashing  

## Author
**Shouryan**
