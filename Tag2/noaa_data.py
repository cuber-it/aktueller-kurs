import requests

# Make HTTP request to get temperature data from NOAA API
temperature_response = requests.get("https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00094728&startDate=1920-01-01&endDate=2019-12-31&dataTypes=TAVG&includeAttributes=true&format=json")

# Check if the request was successful
if temperature_response.status_code == 200:
    # Get temperature data in JSON format
    temperature_data = temperature_response.json()
    print(temperature_data)
