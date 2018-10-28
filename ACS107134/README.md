### 1.管理群組共用資料的權限設計： 

### ˙ 建立群組名稱為： mygroup, nogroup 
groupadd groupname
### ˙ 建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord 
useradd -G groupname username

passwd username

![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/1.JPG)

### ˙ 建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord 
useradd -G groupname username

passwd username

![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/2.JPG)

### ˙ 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限 
mkdir directoryname

chmod 770 directoryname

chgrp groupname directoryname

ll /srv查看確認一下

![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/3.JPG)

### ˙ 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。 

su myuser1
cd
touch
exit

![4](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/4.JPG)

### ˙ 復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作: 

### 雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。 

cp A B (把A複製到B去)
chmod g+s
ll 確認
su nouser1



---------------------------------------分隔線-----------------------------------------

### 2.使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出) 
ps aux | grep rsyslog > /root/process_syslog.txt

![7](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/7.JPG)

---------------------------------------分隔線-----------------------------------------

### 3.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
find /usr/bin -perm /u=s -exec ls -l {} \; > /root/findsuidsgid.txt 
find /usr/sbin -perm /u=s -exec ls -l {} \; >> /root/findsuidsgid.txt 

![8](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/8.JPG)
![9](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-4/ACS107134/9.JPG)


