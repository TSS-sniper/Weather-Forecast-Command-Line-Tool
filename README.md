# Weather Forecast Command-Line Tool
## Introduction:
* A command-line tool in Python that utilizes the OpenWeatherMap API to retrieve and display the current weather forecast for a given city.
* The tool accepts a city name as input, communicates with the OpenWeatherMap API to fetch the weather data, parses the JSON response, and presents the relevant weather information, including the city name, temperature, and description.
* It also includes error handling to handle potential exceptions during the API request and response processes.
### Prerequisites:

- Python 3.x installed on your system
- `requests` library installed (you can install it by running `pip install requests`)
- `geopy` library installed (you can install it by running `pip install geopy`)

### Getting Started:

1. Clone or download this repository to your local machine.
2. Sign up on the [OpenWeatherMap](https://openweathermap.org/) to obtain an API key.
3. Open the `weather_forecast.py` file in a text editor.
4. Replace `"api_key"` with your actual OpenWeatherMap API key.

### Usage:

* Run the command-line tool by executing the `weather_forecast.py` script from the command line and providing a city name as an argument.
## Working:

1. The script constructs the API endpoint URL using the provided city name and your OpenWeatherMap API key.
2. It sends a GET request to the OpenWeatherMap API using the `requests` library.
3. If the response status code is 200, the JSON response is parsed, and relevant weather information is extracted.
4. The extracted weather information, including the city name, temperature, and description, is printed to the console.
## Error Handling:
- If the API request fails, an appropriate error message is displayed.
- If the API response status code is not 200, an error message with the status code is shown.
- If no city name is provided as a command-line argument, an error message is displayed.
## Ouput:

![ss_Wcli](https://github.com/TSS-sniper/Weather-Forecast-Command-Line-Tool/assets/121627136/95e49d6d-4c41-457f-95fa-5a897ab77177)
