## About

Using Githubs API "https://api.github.com/users/{username}/{tag}" program loads users followers
and following, saving them in json files. User can choose to see whos following them or who they are following. 

--username [username] --tag notfollowingme  
will return who you are following but are not following you back 

--username [username] --tag followingme  
will return who is following you but you are not following back  

--username [username] --tag getdata  
will go out and retrieve users followers and following via GITHUB API and save to json file for parsing

## Example

![Screenshot 2024-02-19 164528](https://github.com/Beau28713/GitHub_Who_Is_Following_you/assets/65408911/6b213a05-84ca-486a-b549-1d6fef110180)
