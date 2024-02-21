import json
import requests
from rich import print


def scrape_webpage(username: str, tag: str) -> list:
    """This function scrapes the data from the github api and saves it to a json file.

    Args:
        username (str): user name to seaarch for
        tag (str): tag to be used

    Returns:
        list: json list of followers and following
    """
    followers_url = f"https://api.github.com/users/{username}/followers"
    following_url = f"https://api.github.com/users/{username}/following"
    followers_response = requests.get(followers_url)
    following_response = requests.get(following_url)

    if following_response.status_code == 200 and followers_response.status_code == 200:
        following_data = following_response.json()
        followers_data = followers_response.json()

        with open("followers.json", "w") as followers_file, open(
            "following.json", "w"
        ) as following_file:
            json.dump(followers_data, followers_file, indent=2)
            json.dump(following_data, following_file, indent=2)
        print(
            "[bold green]Data has been successfully scraped and saved to followers.json and following.json[/bold green]"
        )
    else:
        return []


def read_json_files() -> list:
    """This function reads the json files and returns the data in a list format.

    Returns:
        list: followers_list, following_list
    """
    with open("followers.json", "r") as file:
        data = json.load(file)
        followers_list = [person["login"] for person in data]

    with open("following.json", "r") as file:
        data = json.load(file)
        following_list = [person["login"] for person in data]

    return followers_list, following_list


def not_following_me():
    """This function checks if the people you are following are not following you back.
    """
    followers, following = read_json_files()

    for person in following:
        if person not in followers:
            print(f"[bold yellow]{person} is not following you back![/bold yellow]")


def following_me():
    """This function checks if the people following you are not being followed back by you.
    """
    followers, following = read_json_files()

    for person in followers:
        if person not in following:
            print(
                f"[bold yellow]{person} is following you, but you are not following them back![/bold yellow]"
            )
