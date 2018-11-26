#authority and operation of the group 
##workflow 1
 - 1 use groupadd to add mygroup and nogroup   
 - 2  use useradd to add myuser1, myuser2, myuser3  
 - 3  use passwd to set up password      
 - 4  use usermod -a -G mygroup myuserX to add the users into the group just created 
 - 5  use useradd to add nouser1, nouser2, nouser3
 - 6  reset password using passwd  
 - 7  use usermod -a -G mygroup myuserX to add the accont into the group 
   
 - 8 use mkdir to add directory "/srv/myproject"  
   
 - 9 use chgrp  mygroup /srv/myproject to change the file
 - 10 use chmod to change the authority of /srv/myproject 
 
 - 11 以 su - myuser1 to switch into myuser1
 - 12  cd /srv/myproject to got forth our file  
   (**must be done step by step**)
 - 13 create a file named myuser1.data after switching  
   
 - 14 log in as root using su - root
 - 15 use cp command to copy the questions request the area
##workflow2
 - 17 use ps aux | grep rsyslog>/root/process_syslog.txt to find something related to rsyslog and access it 
 
##workflow3
 - 18 use find/usr/bin -prem /u=s -exec is -l {} \ ; > /root/findsuidsgid.txt to find out specific file which contains suid in its file name and list them down and divert them to the path of the command
 - 19 use find/usr/bin -prem /u=s -exec is -l {} \ ; >> /root/findsuidsgid.txt find out specific file which contains suid in its file name and list them down and divert them to the path of the command  
 
 - 20 and then cat /root/findsuidsgid.txt to confirm everything we have done above to be successfull 
   and thats it 