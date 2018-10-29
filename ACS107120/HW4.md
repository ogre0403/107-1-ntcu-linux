# 第一題
 1.建立群組名稱為： mygroup, nogroup
   以root的身分登入
   groupadd mygroup
   groupadd nogroup
 
 2.建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
   useradd myuser1
   passwd myuser1
   設定密碼為 MyPassWord
   chgrp mygroup
   
   useradd myuser2
   passwd myuser2
   設定密碼為 MyPassWord
   chgrp mygroup
   
   useradd myuser3
   passwd myuser3
   設定密碼為 MyPassWord
   chgrp mygroup
   
 3.建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
   useradd nouser1
   passwd nouser1
   設定密碼為 MyPassWord
   chgrp nogroup
   
   useradd nouser2
   passwd nouser2
   設定密碼為 MyPassWord
   chgrp nogroup
   
   useradd nouser3
   passwd nouser3
   設定密碼為 MyPassWord
   chgrp nogroup
   
 4.建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，
   且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
   cd / (回到根目錄)
   mkdir srv(建立srv資料夾)
   cd srv(進入srv)
   mkdir myproject(建立myproject)
   chgrp mygroup myproject
   chmod u=rwx, g=rwx, o= myproject
   
 5.暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，
   嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。 
   su - myuser1 (切換到myuser1的身分)
   cd / (到家目錄)  
   cd srv (進入srv)
   cd myproject (進入myproject)
   touch myuser1.data (建立myuser1.data的檔案)
   exit (登出)
   
 6.複製/usr/bin/ls至/usr/local/bin/myls
   cp /usr/bin/ls /usr/local/bin/myls
   
 7.切換至nouser1
   su - nouser1
   ls 不能執行
      
   
# 第二題
 1.ps aux |grep rsyslog
   找出PID為950
   command為/usr/bin/rsyslogd -n
 
 2.top
   找出PR為20
   NI為0
 
 3.資訊轉存到 /root/process_syslog.txt 檔案中
   ps aux | grep rsyslog > /root/process_syslog.txt
   vi process_syslog.txt 
    
# 第三題   
 1.find /usr/bin /usr/sbin -perm /4000
 
 2.含有 SUID 的特殊檔案檔名
   chfn
   chsh
   mount
   chage
   gpasswd
   newgrp
   su
   umount
   sudo
   pkexec
   crontab
   passwd
   pam_timestamp_check
   unix_chkpwd
   usernetct1   
   
 3.將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中
   find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; >  /root/findsuidsgid.txt
   vi findsuidsgid.txt
   
   
   
   
   
   
   