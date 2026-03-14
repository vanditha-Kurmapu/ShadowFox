# Dictionary containing cities and their countries
cities = {
    "mumbai": "India",
    "chennai": "India",
    "delhi": "India",
    "sydney": "Australia",
    "melbourne": "Australia",
    "dubai": "UAE",
    "abu dhabi": "UAE"
}

# Taking input from the user
city1 = input("Enter the first city: ").lower()
city2 = input("Enter the second city: ").lower()

# Checking if both cities exist in dictionary
if city1 in cities and city2 in cities:
    if cities[city1] == cities[city2]:
        print("Both cities are in", cities[city1])
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the database")