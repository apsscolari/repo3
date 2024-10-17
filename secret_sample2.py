# APS test
import requests

# Sample API key (dummy for testing purposes)
api_key = "1234567890abcdef1234567890abcdef"

# Sample username and password
username = "testuser"
password = "testpassword123"

def make_request():
    url = "https://api.example.com/data"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Request successful!")
    else:
        print("Failed request")

def main():
    print(f"Using credentials: {username} / {password}")
    make_request()

if __name__ == "__main__":
    main()
