1.

use echo ver command to set up a variable.

and give it a value using 

ver='my kernel version is 3.xx'

use echo $ver to have the value of the variable shown on the screen 

the functio of PATH, environmental variable is the path of search of te executable file : symbol can separate directories from directories.

2.the owner of this file can do everything he wants to this file as well as the group members , while others people can't cuz they only have the authority of r and w meaning they cant get into the directroy but fail to do any modifications in it.

original authority :rw-r--r--.

chmod u=rwx,go=rwx script.sh

chmod 777 script.sh

3.

in hard link more than one file names may actually end up corresponding to a single set of inode codes,while symbolic link doesn't , in symbolic link one file name will always be upon one unique set of inode codes.

founding 

cd ~user 

ln /etc/hosts hosts.real
(hard link)

cd ~user 

ln -s /etc/hosts hosts.real
(symbolic link)
