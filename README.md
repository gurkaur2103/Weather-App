# Weather-App
# SkyCast: Your Personal Weather Guide
SkyCast is a simple and interactive weather forecasting application built using Python and Tkinter. It provides real-time weather information, including temperature, weather conditions, and dynamic weather icons, using the OpenWeather API.

## Features:-
Real-Time Weather Updates: Fetch live weather data for any city worldwide.
User-Friendly Interface: Easy-to-navigate GUI with a visually appealing layout.
Dynamic Weather Icons: Displays appropriate weather icons based on current conditions (cloudy, rainy, sunny, etc.).
Temperature Conversion: Displays temperature in Celsius with detailed min/max values.
Background Theme: A visually engaging background and theme enhance the app's appearance.

## Requirements:-
Before running the application, ensure you have the following installed:
=>Python (3.7 or above)
=>Required Python libraries:
  #tkinter (comes pre-installed with Python)
  #Pillow (for image handling)
  #requests (for API calls)

To install additional libraries, use:
pip install pillow requests

## Installation:-
Clone the repository or download the source code.

Ensure the images (e.g., bg.webp, cloud_icon.png, rain_icon.webp, sun_icon.jpg, and weather_frame_bg.webp) are present in the specified directory paths in your code or modify the paths to match your system.

Replace the API key in the code with your own OpenWeather API key:
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY").json()
You can obtain an API key from the OpenWeather API website.

## How to Use:-
Launch the application.
Enter the name of the city in the "Enter City" field.
Click the "Get Weather" button to fetch the weather details.
View the weather condition, temperature, and corresponding icon in the weather information frame.

## Project Files:-
Main Script: The Python file containing the GUI and functionality.
Images:
Background image: bg.webp
Weather condition icons: cloud_icon.png, rain_icon.webp, sun_icon.jpg
Weather frame background: weather_frame_bg.webp

## Known Issues:-
Ensure a stable internet connection to fetch API data.
Invalid city names may display "Invalid City" in the weather condition field.
Missing or incorrectly placed image files will result in errors.

## Credits:-
Weather Data: Powered by OpenWeather API.
Icons and Backgrounds: Designed or sourced for project use.
Framework: Built with Python's Tkinter library.

Enjoy using SkyCast for real-time weather updates! 😊
