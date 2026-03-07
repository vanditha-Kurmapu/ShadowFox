# List of cities for each country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask user to enter a city name
city = input("Enter a city name: ")

# Check which country the city belongs to
if city in Australia:
    print(city + " is in Australia")
elif city in UAE:
    print(city + " is in UAE")
elif city in India:
    print(city + " is in India")
else:
    print("City not found in the list")