# Weather Forecast Command-Line Tool #
## Introduction ##
* A command-line tool in Python that utilizes the OpenWeatherMap API to retrieve and display the current weather forecast for a given city.
* The tool accepts a city name as input, communicates with the OpenWeatherMap API to fetch the weather data, parses the JSON response, and presents the relevant weather information, including the city name, temperature, and description.
* It also includes error handling to handle potential exceptions during the API request and response processes.
## Working: ##
* Command-line tool that accepts a city's name and returns the current weather forecast. Leveraging OpenWeatherMap API to fetch weather data and parse it using Python.

  Methodology involved:
  
  1. The script constructs the API endpoint URL using the provided city name and your OpenWeatherMap API key.
  2. It sends a GET request to the OpenWeatherMap API using the requests library.
  3. If the response status code is 200, the JSON response is parsed, and relevant weather information is extracted.
  4. The extracted weather information, including the city name, temperature, and description, is printed on the console.
## Tool Stack Used: ##
* Python
* OpenWeatherMap API
* Python Libraries such as requests, sys, json and geopy.
