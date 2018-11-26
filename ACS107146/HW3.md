#1.
add a new user with "useradd" command
example : useradd examuser



deleting added user command will be userdel 
example : userdel examuser

-r reference will be neede if you wanna home directory to be deleted as well
example : userdel -r examuser

input userdel -r examuser3 deleteexamuser3 account ans directory input id examuser1，check outUID and GID of examuser1 will be 1001 and input adduser -u 1001 examuser1，reestablish examuser1

#2.
add examuser using adduser command as well
copy file to examuser4 using example : cp xxxxx /home/examuser4
using chmod to change authority limits
example : chmod *** *****
create a file using mkdir command
(P.S: they shall be created ine after one.
modify the owner using chown same as to the group --chgrp

using chmod to change authority as follow



#3. 1.use mkdir and r=4,w=2,x=1
Example : mkdir -m 775 /dev/shm/unit05/
or use mkdir to create file and change the authorit using chmod command and ll command can be used to confirm the authority limit

2.input ls -1/dev/shm/unit05/dir[1-4]， result of dir1 can be read 
result of dir2 is executable 
result of dir3 is executable and modifiable 
result of dir4 is the supreme authority that has all of the authority limits

3.input ls -1/dev/shm/unit05/dir1/file[1-4]， result of file1 is readable
that of file3 is readable
that of file3 is modifiable and readable 
result of file 4 has no authority