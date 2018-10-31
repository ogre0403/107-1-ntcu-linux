HW-4
#建立群組名稱為： mygroup, nogroup
解決方法:
(1)輸入groupadd mygroup，再輸入grep mygroup /etc/group，檢查是否建立成功
(2)輸入groupadd nogroup，再輸入grep nogroup /etc/group，檢查是否建立成功

#建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
解決方法:
輸入useradd -G mygroup myuser1、useradd -G mygroup myuser2、useradd -G mygroup myuser3
再輸入 id myuser1,id myuser2,id myuser3檢視myuser1,myuser2,myuser3的群組是否為mygroup
密碼設定的部分: 
(1)輸入echo MyPassWord | passwd --stdin myuser1會出現Changing password for user myuser1和passwd:all authentication tokens updated successfully代表密碼成功設定好
(2)輸入echo MyPassWord | passwd --stdin myuser2會出現Changing password for user myuser2和passwd:all authentication tokens updated successfully代表密碼成功設定好
(3)輸入echo MyPassWord | passwd --stdin myuser3會出現Changing password for user myuser3和passwd:all authentication tokens updated successfully代表密碼成功設定好

#建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
解決方法:
輸入useradd -G nogroup nouser1、useradd -G nogroup nouser2、useradd -G nogroup nouser3
再輸入 id nouser1,id nouser2,id nouser3檢視nouser1,nouser2,nouser3的群組是否為nogroup
密碼設定的部分: 
(1)輸入echo MyPassWord | passwd --stdin nouser1會出現Changing password for user nouser1和passwd:all authentication tokens updated successfully代表密碼成功設定好
(2)輸入echo MyPassWord | passwd --stdin nouser2會出現Changing password for user nouser2和passwd:all authentication tokens updated successfully代表密碼成功設定好
(3)輸入echo MyPassWord | passwd --stdin nouser3會出現Changing password for user nouser3和passwd:all authentication tokens updated successfully代表密碼成功設定好

#建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
**輸入mkdir /srv/myproject，再輸入chgrp mygroup /srv/myproject，再更改權限輸入chmod 770 /srv/myproject，再輸入ls -1d /srv/myproject看看是否權限更改成功

#暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。
**切換myuser1，輸入su myuser1,切換之後輸入cd /srv/myproject，進到目錄時建立一個檔案，輸入mkdir myuser1.data再輸入ls 觀看是否建檔成功，最後輸入cd ..登出

#複製/usr/bin/ls至/usr/local/bin/myls後，完成下列操作
(1)輸入cp /usr/bin/ls /usr/local/bin/myls
(2)檢視自己有沒有複製成功，輸入ll /usr/local/bin/myls
(3)成功會顯示 -rwxr-xr-x. 1 root root 117672 Oct 28 16:23 /usr/local/bin/myls(/usr/local/bin/myls會呈現紅色)
**SUID-對於該程式來說，須具備x的權限
**執行者在執行過程中將會火的該程式群組的權限
(4)輸入sudo chmod u+s /usr/local/bin/myls
(5)輸入檢視ll /usr/local/bin/myls
(6)成功會顯示 -rwxr-xr-x. 1 root root 117672 Oct 28 16:23 /usr/local/bin/myls(/usr/local/bin/myls會呈現紅色)
(7)切換su nouser1
(8)輸入myls /srv/myproject
(9)myuser1.data 成功切換

#使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)
(1)利用grep找尋
輸入-- ps aux | grep rsyslog
找出PID---977，找出command為/usr/bin/rsyslogd-n
(2)輸入ps -l
發現可以查詢PID資料
(3)找出ps -977
發現可以找出command為/usr/bin/rsyslogd-n
(4)接著利用top、ps aux找出PR跟NI的資料
(5)最後儲存資料
(6)輸入ps aux | grep rsyslog > /root/process_syslog.txt
(7)輸入vi process_syslog.txt

#使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
(1)find /usr/bin /usr/sbin -perm /4000
列出全部檔名
chfn,chsh,mount,chage,gpasswd,newgrp,su,umount,sudo,pkexec,crontab,passwd,pam_timestamp_check,uniz_chkpwd,usernetct1
(2)find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;(將權限都列印出來)
(3)存取檔案到findsuidsgid.txt
find /usr/bin /usr/sbin -perm/4000 -exec ls -l {} \; > /root/findsuidsgid.txt
(4)輸入vi findsuidsgid.txt看是否存取成功