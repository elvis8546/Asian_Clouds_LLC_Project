import requests
import os
import uuid

# Kong API URL
KONG_API_URL = "https://your-kong-api-url.com"  # Replace with your Kong API URL

# Function to upload a file and generate a unique CDN URL
def upload(file_path):
    try:
        # Generate a unique asset ID (you can use a UUID for this)
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

# Example usage
if __name__ == "__main__":
    file_to_upload = "path/to/your/file.jpg"
    uploaded_cdn_url = upload(file_to_upload)

    if uploaded_cdn_url:
        # Specify where to save the retrieved file
        save_path = "path/to/save/retrieved/file.jpg"
        
        # Retrieve the file from the CDN
        retrieve(uploaded_cdn_url, save_path)