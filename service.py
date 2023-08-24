import requests

# URL to which you want to send the POST request
url = "https://seniment-shirin.onrender.com/sentiment"

# Data to be sent in the POST request
data = {"review": "even then movie was bad but , action was awesom!!! "}

# Define the headers
headers = {
    "Content-Type": "application/json",  # Specify the content type
}

# Send the POST request with headers
response = requests.post(url, json=data, headers=headers)

print("POST request failed with status code:", response.json())
