import requests

def verify():
    # Matches the notebook usage
    endpoint = "http://localhost:8002/api/events/"
    print(f"Testing connection to {endpoint}...")
    try:
        response = requests.get(endpoint)
        if response.ok:
            data = response.json()
            print(f"SUCCESS: Retrieved {len(data)} events from API.")
            if data:
                print("Sample event:", data[0])
            else:
                print("List is empty (valid response, just no data yet).") 
                print("Try running the data generation in the notebook or via POST.")
        else:
            print(f"FAILED: Status {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"Connection Error: {e}")
        print("Ensure the docker container is running and mapped to port 8002.")

if __name__ == "__main__":
    verify()
