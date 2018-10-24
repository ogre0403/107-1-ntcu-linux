First question

 (一)establish three user first，and they are examuser1,examuser2,examuser3 password is ltlsExam
 **Solution:1.logged in，switch to root 2.establish user account and input program code (useradd examuser1)
 input (passwd examuser1)，there will be (Change password for user examuser1) on the screen
 password input available and double check up，Next,examuser2.examuser3 are supposed to be done as above 

 (二)delete examuser3 in system，delete this account in this home directory in sync with mail files
 **solution--use-r as a reference，input userdel -r examuser3

 (三)examuser1 if by accident deleted by the root. still the home directory as well as the mail files are preserved.refer to the file that are possibly preserved by this home directory UID and GID， try to recuperate all the account with UID/GID using ItIsExam form
 **solution:input useradd -u (UIDprogram code) -U examuser1 it will looks as followed 

 Second question

 (一)set up account examuser4
 **solution:input useradd examuser4 and input passwd examuser4 then password input will be allowed ok to mae a confirmation later 

 (二)use root to /etc/securetty copy to examuser4，and the account shall be able to fully get access to the file ，(that is overall authority).
 solution:first switch to root path，and then type chmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty，switch to cd /home/examuser4,and input ll to see if work 

 (三)set up /examdata/change.txt as an empty file，owner of this file is sshd，group is  users，sshd r, w permitted，users group members can read ，while others don't.
     
 **solution:set up anempty file， input mkdir examdata,click into examdata from cd，touch change.txt input ls see if it works
 change user name chown sshd change.txt，and input group name chgrp users change.txt，change authority using chmod u=rw,g=r,o= change.txt，11 see if it works

 Third question
 (一)use root to creat the following files and authority limit
 **solution: input cd /dev，enter and input shm，click into shmlayer establishing mkdir unit05，modify authority limit of shm in unit05，input chmod u=rwx,g=rwx,o=rx unit05
 anad input cd unit05 set up this inside dir1,dir2,dir3,dir4 and modify authority limit (unit05 layer mkdir dir1,andchmod u=rwx,g=rx,o=r dir1)(在unit05 layer mkdir dir2,再來chmod u=rwx,g=rx,o=x dir2)
 (在unit05 layer mkdir dir3,andchmod u=rwx,g=rx,o=rx dir3)(在unit05 layer mkdir dir4,and chmod u=rwx,g=rwx,o=rwx dir4)and input ll seeif it works
 and set up dir1-4 的file (input cp /etc/hosts dev/shm/unit05/dir1/file1 ge tinto dir1 modify limit chmod u=rw,g=r,o=r file1在cd ..back unit05)(input cp /etc/hosts dev/shm/unit05/dir2/file2 get into dir2 modify chmod u=rw,g=r,o=r file2在cd ..back unit05 )
 (input cp /etc/hosts dev/shm/unit05/dir3/file3 get into dir3 modify limit chmod u=rw,g=rw,o=rw file3 cd ..unit05 )(input cp /etc/hosts dev/shm/unit05/dir4/file4 get inot dir4 modify limit chmod u=rw,g=,o= file4 cd ..back unit05 )
 (二)
 use ls -l /dev/shm/unit05/dir[1-4] elaborate on possible causes of it according to the input 
 **3,4 can be run while others dont't
 (三)use ls -l /dev/shm/unit05/dir1/file1 ，run dir1/file1 ~ dir4/file4 based on aforementioned file name ，elaborate it based on output？
 none of them could be run cuz none of them has the authority
 (四)use  vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，attemy saving  (forcibly store)，explain why can be or can't be saved？
 only the third one is capable for it is the only one that possesses authority to modify