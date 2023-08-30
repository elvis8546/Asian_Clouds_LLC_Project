import requests
import os
import uuid

KONG_API_URL = "http://localhost:8000/test-CDN-api"  #The KONG API URL which build from Kong API Gateway's docker-compose!

# Function to upload a file and generate a unique CDN URL
def upload(file_path):
    try:
        asset_id = str(uuid.uuid4())

        # Prepare the file for uploading
        with open(file_path, 'rb') as file:
            files = {'file': (asset_id, file)}

            # Make a POST request to upload the file
            response = requests.post(f"{KONG_API_URL}/upload", files=files)

        # Check if the upload was successful (you can adjust the status code as needed)
        if response.status_code == 200:
            # Construct the CDN URL for the uploaded asset
            cdn_url = f"{KONG_API_URL}/cdn/{asset_id}"
            return cdn_url
        else:
            print(f"Upload failed with status code {response.status_code}")
            return None

    except Exception as e:
        print(f"Error uploading file: {str(e)}")
        return None

# Function to retrieve a file from the CDN
def retrieve(cdn_url, save_path):
    try:
        # Make a GET request to retrieve the file
        response = requests.get(cdn_url)

        # Check if the retrieval was successful (you can adjust the status code as needed)
        if response.status_code == 200:
            # Save the retrieved file
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"File retrieved and saved at {save_path}")
            return True
        else:
            print(f"File retrieval failed with status code {response.status_code}")
            return False

    except Exception as e:
        print(f"Error retrieving file: {str(e)}")
        return False
