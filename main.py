import requests
import json

def scrape_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return "No data found"
    
def main():
    url = "https://api.github.com/users/beau28713/followers"
    data = scrape_webpage(url)
    if data:
        print(json.dumps(data, indent=2))
    else:
        print("Failed to fetch data from the URL")
        
if __name__ == "__main__":
    main()