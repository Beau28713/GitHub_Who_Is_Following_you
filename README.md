## About

Utilizing GitHub's API at "https://api.github.com/users/{username}/{tag}", the program retrieves a user's followers and those they are following, storing this data in JSON files. Users have the option to view who is following them or whom they are following.

To check who you are following but are not followed back:
```shell
--username [username] --tag notfollowingme
```
To identify who is following you but you are not following back:
```shell
--username [username] --tag followingme
``` 
To fetch and save the user's followers and those they are following via the GitHub API:
```shell
--username [username] --tag getdata
```

## Example

![Screenshot 2024-02-19 164528](https://github.com/Beau28713/GitHub_Who_Is_Following_you/assets/65408911/6b213a05-84ca-486a-b549-1d6fef110180)
