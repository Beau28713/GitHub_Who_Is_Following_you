## About 
Using Githubs API "https://api.github.com/users/{username}/{tag}" program will load users followers  
and who the user is following. It then returns who is not following the user back. 

## Example
```
(base) C:\Users\clark\Documents\code\python\GitHub_Who_Is_Following_you>python -m main
followers has been written to the file
Reading the json files...
Checking who is not following you back...
PyBites-Open-Source is not following you back!
```

## Future plans
Will make this into an CLI package for easier use.
Allowing user to enter command and options at CLI so the code wont have to be
Changed. Right now the user inputs has to be physically changed in the code (Not Good). 
