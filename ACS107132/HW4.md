##一
#1-1建立群組名稱為： mygroup, nogroup
*"groupadd mygroup", "groupadd nogroup"，建立mygroup, nogroup群組

#1-2建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
*"useradd -g mygroup [myuser1, myuser2, myuser3]"，建立myuser1, myuser2, myuser3並加入mygroup群組
*"passwd [myuser1, myuser2, myuser3]"設定密碼為MyPassWord

#1-3建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
*跟1-2的步驟一樣，群組跟使用者名稱不一樣而已
+"id"指令可以確定使用者資料

#1-4建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
*建立一個名為 /srv/myproject 的目錄:"cd srv"→"mkdir myproject"
*"chgrp mygroup myproject"設定mygroup的群組為mygroup→"chmod 770 myproject"設定權限mygroup可以完整使用，其他使用者不能使用

#1-5暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1
*"su myuser1"登入myuser1→"cd srv"→"cd myproject"→"vi myuser1.data"建立myuser1.data檔案
*"exit"登出

#1-6複製/usr/bin/ls至/usr/local/bin/myls後，完成下列操作
*"cp /from/usr/bin/ls /to/usr/local/bin/myls"複製
*"su nouser1"登入nouser1→"myls /srv/myproject"

##二
#將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND
*"ps aux | grep rsyslog"→PID:950, command:/usr/bin/rsyslogd -n
*"top"→PR:20, NI:0
#將資訊轉存到 /root/process_syslog.txt 檔案中
*"ps aux | grep rsyslog > /root/process_syslog.txt"→"vi process_syslog.txt"

##三
#使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名
*"find /usr/bin /usr/sbin -perm /4000"
+chfn
+chsh
+mount
+chage
+gpasswd
+newgrp
+su
+umount
+sudo
+pkexec
+crontab
+passwd
+pam_timestamp_check
+unix_chkpwd
+usernetct1
#使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中
*"find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; >  /root/findsuidsgid.txt"
*"vi findsuidsgid.txt"