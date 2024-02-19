import typer
import read_json
from typing import Annotated


def main(
    username: Annotated[str, typer.Option(help="User ID to look up.")] = "",
    tag: Annotated[
        str, typer.Option(help="Options to be used: notfollowingme or followingme.")
    ] = "",
):

    typer.Option(
        help="The username of the GITHUB user to scrape data from.", show_default=True
    )

    tag_dic = {
        "getdata": read_json.scrape_webpage,
        "notfollowingme": read_json.not_following_me,
        "followingme": read_json.following_me,
    }

    option = tag_dic.get(tag)

    if option is None:
        raise ValueError(
            f"Invalid tag, {tag} not in the list of tags. Please use' 'getdata', 'notfollowingme', or 'followingme' as tags."
        )

    (tag_dic.get(tag)(username, tag) if tag == "getdata" else tag_dic.get(tag)())


if __name__ == "__main__":
    typer.run(main)
