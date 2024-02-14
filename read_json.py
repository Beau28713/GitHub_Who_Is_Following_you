import json


def read_followers():
    with open("followers.json", "r") as file:
        data = json.load(file)
    return data


def read_following():
    with open("following.json", "r") as file:
        data = json.load(file)
    return data


def main():
    followers = read_followers()
    following = read_following()
    following_list = [person["login"] for person in following]
    followers_list = [person["login"] for person in followers]
    
    for person in following_list:
        if person not in followers_list:
            print(f"{person} is not following you back!")


if __name__ == "__main__":
    main()
