import requests
import json

category = 'failure'
API_KEY = "O7d+tdG0aASESu32dATg1A==zwWd1XlfBx49IueN"
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})

# Check if the request was successful (status code 200) before proceeding
if response.status_code == 200:
    # Parse the JSON response into a list of dictionaries
    data = json.loads(response.text)

    # Ensure that the list is not empty before accessing the "quote" key
    if data and isinstance(data, list):
        quote_value = data[0]["quote"]
        print(quote_value)
    else:
        print("No quotes found in the program.")
        print("Try again.")
        print("Test 1.")
        print("Test 2.")
else:
    print(f"Error: {response.status_code} - {response.text}")
