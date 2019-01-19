#HW9  
###1.  
只需在CentOS 7 鍵入以下yum命令  
 **yum install epel-release**
![](https://ppt.cc/fx7b7x@.png)
###2.  
安裝完成後，使用以下yum repolist命令查看epel repo  
**yum repolist**  
![](https://ppt.cc/fIstZx@.png)

###3.  
要列出名為epel的repo下的所有可用包，請輸入：  
**yum --disablerepo="*" --enablerepo="epel" list available**  
![](https://ppt.cc/fSa0Lx@.png)
###4.  
然後使用搜尋  
**yum search htop** 
![](https://ppt.cc/fdkwEx@.png)
###5.  
列出更多有關htop的信息用  
**yum info htop**
![](https://ppt.cc/fgjqIx@.png)
###6.  
最後安裝htop使用  
**yum install htop**  
![](https://ppt.cc/fNtRox@.png)