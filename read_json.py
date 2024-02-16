import json
import requests
from rich import print

def scrape_webpage(username: str, tag: str):
    url = f"https://api.github.com/users/{username}/{tag}"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return "No data found"


def get_followers(username: str, tag: str):
    data = scrape_webpage(username, tag)
    with open("followers.json", "w") as file:
        json.dump(data, file, indent=2)


def get_following(username: str, tag: str):
    data = scrape_webpage(username, tag)
    with open("following.json", "w") as file:
        json.dump(data, file, indent=2)


def read_followers():
    with open("followers.json", "r") as file:
        data = json.load(file)
        followers_list = [person["login"] for person in data]
    return followers_list


def read_following():
    with open("following.json", "r") as file:
        data = json.load(file)
        following_list = [person["login"] for person in data]
    return following_list


def not_following_me():
    followers = read_followers()
    following = read_following()

    for person in following:
        if person not in followers:
            print(f"[bold yellow]{person} is not following you back![/bold yellow]")


def following_me():
    followers = read_followers()
    following = read_following()

    for person in followers:
        if person not in following:
            print(f"[bold yellow]{person} is following you, but you are not following them back![/bold yellow]")
