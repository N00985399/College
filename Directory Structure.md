# Directories Chapter 5 | Unix & Linux
#### Start: 09/16/2024 

## Example of Directory Structure for Linux
```
.
└── root/
    ├── bin/
    │   └── ...
    ├── lib/
    │   └── ...
    ├── usr/
    │   ├── david/
    │   │   └── ...
    │   ├── daniel/
    │   │   └── ...
    │   └── gabriel/
    │       └── ...
    └── dev/
        └── ...
```

## Commands
### cd
'cd' stands for "Change Directory" and allows you to change the working directory to a desired target. ex) ```$ cd ./usr/daniel/home/desktop```
- running 'cd' with no arguments will assign your working directory to the previous level. ie) running ```cd``` while within ```./usr/daniel/home/desktop``` would set yout directory to ```./usr/daniel/home```
- typing 'cd' and pressing ``[TAB]`` will show you the relative paths to the local directories and files.
### pwd
'pwd' stands for "Print Working Directory" which prints the current directory that commands are being executed within. ex) ```$ pwd```
### mkdir
'mkdir' stands for "Make Directory" and is used to create a directory within the current path. ex) ```$ mkdir "Work Assignments"``` would make a Directory called ```Work Assignments```

### rmdir
'rmdir' stands for "Remove Directory" and is used to delete a directory within the current path. ex) ```$ rmdir "Work Assignments"``` would make a delete the relative directory [Unless an absoute path is provided] called ```Work Assignments```
### ls
The ls command in Linux is used to list the contents of a directory.
### touch
'touch' makes a file within the current directory. ex) ```touch "List of Employee Addresses"``` would make a blank unextensionated file named "List of Employee Addresses"
## Paths
Paths are a means of locating and referencing files and directories.  
### Absoute
An absoute pathname (full path) gives the explict, or absoute directory route to a file or target directory. 
  ```
        . [WE ARE HERE]
        └── usr/
            └── daniel/
                └── home/
                    └── desktop/
                            └── favorate_movies.txt
  ```
The ABSOUTE path for favorate_movies.txt would be ./usr/daniel/home/desktop/favorate_movies.txt

### Relative
A relative pathname (immediate directory) gives the relative, or local path to a file or target directory.
```
        .
        └── usr/
            └── daniel/
                └── home/
                    └── desktop [WE ARE HERE]/
                            └── favorate_movies.txt
```
Since we are within the same directory as favorate_movies.txt. We can do \cd favorate_movies.txt to access favorate_movies.txt.

## 5.3.2 The Home Directory 

- The System adminstrator creates all user accounts on the system and associates each user account with a particular directory.
- This Directory is the home directory.
- The log on process places you into your home directory

## 5.3.3 The Working Directory

- The Working Directory is where all commands are being executed within.
- The name of the current working directory is the last directory in the absolute path.
- you can do **pwd** to obtain the current working directory.


