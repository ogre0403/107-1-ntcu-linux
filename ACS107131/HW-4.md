## 1-1 建立群組名稱為： mygroup, nogroup   
   
#### * groupadd 群組名稱  
   
## 1-2 建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord   
## 1-3 建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord  
   
#### * useradd -G 群組名稱 用戶名稱   
#### * passwd 用戶名稱   
![1](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/1.png?raw=true)   
#### * 檢查是否成功 tail -數字(顯示多少組項目) /etc/group   
![2](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/2.PNG?raw=true)   
   
## 1-4 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新## 建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限   
   
#### * cd /srv   
#### * 建立目錄 mkdir myproject   
#### * ll   
#### * 更改擁有檔案的群組 chgrp mygroup myproject   
#### * 更改權限 chmod u=rwx,g=rwx,o= myproject   
![3](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/3.PNG?raw=true)   
![4](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/4.PNG?raw=true)   
   
## 1-5 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。   
   
#### * su - myuser1   
#### * cd /srv/myproject   
#### * 建立檔案 touch myuser1.data   
#### * 檢查 ls   
#### * 登出 exit  
![5](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/5.PNG?raw=true)   
   
## 1-6 復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作   
   
## 雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行/usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行到【myls/srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。      
     
#### * 複製 cp /usr/bin/ls /usr/local/bin/myls   
#### * 更改權限 chmod u+s /usr/local/bin/myls  
#### * 切換到nouser1      
####   su - nouser1  
#### * myls /srv/myproject     
![6](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/6.PNG?raw=true)   
   
## 2 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, 
## PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)  
  
#### * ps aux | grep rsyslog > /root/process_syslog.txt  
#### * 檢查是否成功    
####   cd /root   
####   cat process_syslog.txt 顯示內容    
![02](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/02.PNG?raw=true)   
   
## 3 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令 用法，以及使透過重導向符號>輸出檔案)    
    
#### * find /usr/bin -perm /u=s -exec ls -l {} \; > /root/findsuidsgid.txt   
#### * find /usr/sbin -perm /u=s -exec ls -l {} \; >> /root/findsuidsgid.txt(>>是繼續文件內容)   
#### * 檢查是否成功    
####  cat /root/findsuidsgid.txt    
![03](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-4/ACS107131/03.PNG?raw=true)     