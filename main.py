import typer
import read_json


def main(username: str = "" , tag: str = ""):
    if tag == "followers":
        read_json.get_followers(username, tag)
        print("followers has been written to the file")

    elif tag == "following":
        read_json.get_following(username, tag)
        print("following has been written to the file")

    elif tag == "not_following_me":
        read_json.not_following_me()

    elif tag == "following_me":
        read_json.following_me()

    else:
        print("Invalid tag")


if __name__ == "__main__":
    typer.run(main)
