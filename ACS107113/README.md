# HW4
#### 第一題
+ 1.建立群組名稱為： mygroup, nogroup
![GITHUB](https://imgur.com/MmCsqE2.jpg"git圖示")
+ 切換成root權限
![GITHUB](https://imgur.com/f2iXbHp.jpg"git圖示")
+ 用groupadd 創建兩個新群組
+ 2.建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
![GITHUB](https://imgur.com/BjVnGCE.jpg"git圖示")
+ 用useradd的指令依序建立myuser1,2,3
![GITHUB](https://imgur.com/DlNlzTj"git圖示")
+ 將myuser1,2,3加入mygroup ->usermod -g mygroup myuser1
![GITHUB](https://imgur.com/GZAmrzn.jpg"git圖示")
![GITHUB](https://imgur.com/mXHAXPv.jpg"git圖示")
![GITHUB](https://imgur.com/tSaKq7Z.jpg"git圖示")
+ 用passwd將myuser1,2,3密碼為MyPassWord
+ 3.建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
![GITHUB](https://imgur.com/bGZVDfm.jpg"git圖示")
+ 用useradd -g nouser nouser1的指令依序建立nouser1,2,3，並同時將nouser1,2,3加入mygroup
![GITHUB](https://imgur.com/BDBRR6z.jpg"git圖示")
![GITHUB](https://imgur.com/ofRPrfW.jpg"git圖示")
![GITHUB](https://imgur.com/oAmWOrr.jpg"git圖示")
+ 用passwd將nouser1,2,3密碼為MyPassWord
+ 4.建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
![GITHUB](https://imgur.com/VfpkTA0.jpg"git圖示")
+ 建立/srv/myproject 的目錄，用mkdir /srv/myproject
+ 再將該目錄改變到mygroup群組，chgrp mygroup /srv/myproject
![GITHUB](https://imgur.com/PZaBWOz.jpg"git圖示")
+ 改變權限，chmod 770 /srv/myproject
+ 5.暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1
![GITHUB](https://imgur.com/BF2oEHr.jpg"git圖示")
+ 切換到myuser1帳號，su myuser1
+ 再切換到/srv/myproject 的目錄下，cd /srv/myproject
![GITHUB](https://imgur.com/tZPA09M.jpg"git圖示")
+ 在該目錄下切換成root權限
+ 再創建myuser1.data，mkdir myuser1.data
![GITHUB](https://imgur.com/eWer8Rb.jpg"git圖示")
+ 退出目錄，cd ..
+ 6.復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作
![GITHUB](https://imgur.com/9W5sFIi.jpg"git圖示")
+ 輸入cp /usr/bin/ls /usr/ocal/bin/myls
+ 再輸入ll /usr/local/bin/myls，檢視是否成功
#### 第二題
+ 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)
![GITHUB](https://imgur.com/XEDnTIw.jpg"git圖示")
+ 輸入ps aux | grep rsyslog檢視
![GITHUB](https://imgur.com/CGxCGSQ.jpg"git圖示")
+ 輸入ps -l，檢視PID、PRI、NI、CMD
![GITHUB](https://imgur.com/jHMwFPd.jpg"git圖示")
![GITHUB](https://imgur.com/Zafdzop.jpg"git圖示")
![GITHUB](https://imgur.com/HY25zi9.jpg"git圖示")
+ 利用top、ps aux找出PR跟NI的資料
![GITHUB](https://imgur.com/MKWCXE3.jpg"git圖示") 
+ 輸入ps aux | grep rsyslog > /root/process_syslog.txt
![GITHUB](https://imgur.com/lke37iq.jpg"git圖示")
+ 輸入vi process_syslog.txt檢視
#### 第三題
+ 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
![GITHUB](https://imgur.com/oPA3E76.jpg"git圖示")
+ 輸入find /usr/bin /usr/sbin -perm /4000，列出檔名，chfn,chsh,mount,chage,gpasswd,newgrp,su,umount,sudo,pkexec,crontab,passwd,pam_timestamp_check,uniz_chkpwd,usernetct1
+ find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \，列出權限
+ find /usr/bin /usr/sbin -perm/4000 -exec ls -l {} \; > /root/findsuidsgid.txt，將檔案存到findsuidsgid.txt
+ 輸入vi findsuidsgid.txt看是否存取成功