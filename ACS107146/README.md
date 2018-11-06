#hw5   procedure


 
##Q1 connection and creation of the file 


 
### find out ln /etc/hosts the code of inode  


 
 - using  ls -li /etc/hosts this command to find out  code "Inode"  


 
 - the code after exwcution is 4213160 


 
### making sure how many file are used together with inode 


 
 - third row says 1 representing only a single file name using this inode  


 
##Q2 estabilish solid connection 


 
### find out ln /etc/hosts /srv/hosts.hard the code of inode  


 
 - using  ln /etc/hosts /srv/hosts.hard to found hardware connection 


 
 - use  ls -li /srv/hosts.hard to find out code "Inode"    


 
 - the codes found will also be 4213160 


 
and then do exactly the same step as aforementioned 



 
##Q3 found symbol connection


 
### find out ln /etc/hosts /srv/hosts.hard the code  inode  


 
 - found symbol connection with ln /etc/hosts /srv/hosts.soft


 
 - find the code of incode using this command ls -li /srv/hosts.soft


 
 - result will be 13029050 


 
### make sure how many common file are being usede inode 


 
 - turns out only a file using 13029050 inode