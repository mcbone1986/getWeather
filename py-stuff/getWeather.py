pip install requests
pip install beautifulsoup4

#import requests
#from bs4 import BeautifulSoup

#url = "https://weather.com/weather/today/l/67b17b84c87e54a949be2f54b48b1712d207debdd7cf6d4b981399b27751c2c1"

# Send a GET request to the URL
#response = requests.get(url)
#print(response.txt)
# Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Locate the div with temperature information
#     temp_div = soup.find('div', class_='WeatherDetailsListItem--wxData--kK35q')

#     if temp_div:
#         # Extract High and Low temperatures
#         high_temp = temp_div.find_all('span', {'data-testid': 'TemperatureValue'})[0].get_text()
#         low_temp = temp_div.find_all('span', {'data-testid': 'TemperatureValue'})[1].get_text()

#         # Print the results
#         print(f"High Temperature: {high_temp}°")
#         print(f"Low Temperature: {low_temp}°")
#     else:
#         print("Temperature information not found on the page.")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

