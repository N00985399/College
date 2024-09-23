USER
R = 4
W = 2
X = 1

GROUP
R = 4
W = 2
X = 1

OTHERS
R = 4
W = 2 
X = 1


653 -rw-r---wx
157 ---xr-xrwx
777-rwxrwxrwx
000 ----------

rwx rwx rwx = 111 111 111
rw- rw- rw- = 110 110 110
rwx --- --- = 111 000 000

rwx = 111 in binary = 7
rw- = 110 in binary = 6
r-x = 101 in binary = 5
r-- = 100 in binary = 4

Value 	Meaning
777 	(rwxrwxrwx) No restrictions on permissions. Anybody may list files, create new files in the directory and delete files in the directory. Generally not a good setting.
755 	(rwxr-xr-x) The directory owner has full access. All others may list the directory, but cannot create files nor delete them. This setting is common for directories that you wish to share with other users.
700 	(rwx------) The directory owner has full access. Nobody else has any rights. This setting is useful for directories that only the owner may use and must be kept private from others.
666 	(rw-rw-rw-) All users may read and write the file.
644 	(rw-r--r--) The owner may read and write a file, while all others may only read the file. A common setting for data files that everybody may read, but only the owner may change.
600 	(rw-------) The owner may read and write a file. All others have no rights. A common setting for data files that the owner wants to keep private.

