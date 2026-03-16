import requests
import os

# Test edge cases for the Flask API
def test_edge_cases():
    url = 'http://localhost:5000/convert'

    # Test 1: No file uploaded
    print("Testing: No file uploaded")
    try:
        response = requests.post(url, files={})
        print(f"Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

    # Test 2: Invalid file (non-image)
    print("\nTesting: Invalid file (text file)")
    try:
        with open('requirements.txt', 'rb') as f:
            files = {'image': f}
            response = requests.post(url, files=files)
        print(f"Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

    # Test 3: Empty filename
    print("\nTesting: Empty filename")
    try:
        files = {'image': ('', b'', 'image/jpeg')}
        response = requests.post(url, files=files)
        print(f"Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_edge_cases()
