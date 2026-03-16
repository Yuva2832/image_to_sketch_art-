import requests

# Test the Flask API endpoint '/convert'
def test_api_endpoint():
    url = 'http://localhost:5000/convert'
    file_path = 'sketches/sketch_yuva 1.jpg'

    try:
        with open(file_path, 'rb') as f:
            files = {'image': f}
            response = requests.post(url, files=files)

        if response.status_code == 200:
            print("API test successful. Status code: 200")
            # Save the response content as image
            with open('test_api_output.png', 'wb') as f:
                f.write(response.content)
            print("Sketch saved to test_api_output.png")
        else:
            print(f"API test failed. Status code: {response.status_code}")
            print(f"Response: {response.text}")

    except Exception as e:
        print(f"Error during API test: {e}")

if __name__ == "__main__":
    test_api_endpoint()
