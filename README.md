## About

Using Githubs API "https://api.github.com/users/{username}/{tag}" program loads users followers
and following, saving them in json files. User can choose to see whos following them or who they are following. 

--username [username] --tag notfollowingme  
will return who you are following but are not following you back 

--username [username] --tag followingme  
will return who is following you but you are not following back  

## Example

```
(base) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username beau28713 --tag notfollowingme
PyBites-Open-Source is not following you back!
JohnMwendwa is not following you back!

(base) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username beau28713 --tag followingme
roblight is following you, but you are not following them back!
mbahomaid is following you, but you are not following them back!

(base) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username beau28713 --tag getdata
```
