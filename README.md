## About

Using Githubs API "https://api.github.com/users/{username}/{tag}" program will load users followers
and who the user is following. It then returns who is not following the user back.

## Example

```
(pybites) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username Beau28713 --tag followers
followers has been written to the file
--------------------------------------------------------------------------------------------------------------------------------------
(pybites) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username Beau28713 --tag following
following has been written to the file
--------------------------------------------------------------------------------------------------------------------------------------
(pybites) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username Beau28713 --tag not_following_me
PyBites-Open-Source is not following you back!
peter-kimanzi is not following you back!
tulna07 is not following you back!
----------------------------------------------------------------------------------------------------------------------------------------
(pybites) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python main.py --username Beau28713 --tag following_me
roblight is following you, but you are not following them back!
mbahomaid is following you, but you are not following them back!
rajuranjan00 is following you, but you are not following them back!
--------------------------------------------------------------------------------------------------------------------------------------
(pybites) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>
```
