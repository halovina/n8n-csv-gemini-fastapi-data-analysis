import requests

# The n8n webhook URL will be placed here
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/ac12b28a-638f-473a-b673-1108aaca56ea" 

# The name of the file to be uploaded
file_path = "sales_data.csv"

try:
    with open(file_path, "rb") as f:
        # 'file' is the field name that will be received by n8n
        files = {"file": (file_path, f, "text/csv")}
        
        print(f"Sending {file_path} to n8n webhook...")
        response = requests.post(N8N_WEBHOOK_URL, files=files)
        response.raise_for_status()  # This will raise an error if the status code is not 2xx

    print("File sent successfully!")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except requests.exceptions.RequestException as e:
    print(f"Error while sending file: {e}")