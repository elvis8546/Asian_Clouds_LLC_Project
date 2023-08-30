from cdn_functions import upload, retrieve

# Example usage
if __name__ == "__main__":
    file_to_upload = "path/to/your/file.jpg"
    uploaded_cdn_url = upload(file_to_upload)

    if uploaded_cdn_url:
        # Specify where to save the retrieved file
        save_path = "path/to/save/retrieved/file.jpg"
        
        # Retrieve the file from the CDN
        retrieve(uploaded_cdn_url, save_path)