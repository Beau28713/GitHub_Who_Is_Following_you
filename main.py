import typer
import read_json


def main(username: str = "", tag: str = ""):

    tag_dic = {
        "followers": read_json.get_followers,
        "following": read_json.get_following,
        "not_following_me": read_json.not_following_me,
        "following_me": read_json.following_me,
        
    }
    try: 
        (
            tag_dic.get(tag, "invalid tag")(username, tag)
            if tag == "followers" or tag == "following"
            else tag_dic.get(tag, "invalid tag")()
        )
    except BaseException as e:
        print("invalid tag, tag not in the list of tags. Please use 'followers', 'following', 'not_following_me', or 'following_me' as tags.")

if __name__ == "__main__":
    typer.run(main)
