## About

Using Githubs API "https://api.github.com/users/{username}/{tag}" program will load users followers
and who the user is following. It then returns who is not following the user back.

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
