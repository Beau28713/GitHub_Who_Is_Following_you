import requests
import json
import read_json


def scrape_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return "No data found"


def get_followers(data: json):
    with open("followers.json", "w") as file:
        json.dump(data, file, indent=2)


def get_following(data: json):
    with open("following.json", "w") as file:
        json.dump(data, file, indent=2)


def main(username: str, tag: str):
    url = f"https://api.github.com/users/{username}/{tag}"
    data = scrape_webpage(url)

    if data:
        if tag == "followers":
            print("followers has been written to the file")
            get_followers(data)
        elif tag == "following":
            print("following has been written to the file")
            get_following(data)
        else:
            print("Invalid tag")

    else:
        print("Failed to fetch data from the URL")


if __name__ == "__main__":
    main("beau28713", "followers")
    print("Reading the json files...")
    print("Checking who is not following you back...")
    read_json.main()