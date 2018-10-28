## 管理群組
1.建立群組
   * groupadd mygroup
   * groupadd nogroup
2.建立新使用者+群組
   * useradd -G mygroup myuser1~3
   * useradd -G mygroup nouser1~3
     -G:指定群組
   * passwd myuser1~3 設定密碼
   * passwd nouser1~3 設定密碼
3.檢查
   * id myuser1
      uid=1004(myuser1) gid=1006(myuser1) groups=1006(myuser1),1004(mygroup)
   * id myuser2
      uid=1005(myuser2) gid=1007(myuser2) groups=1007(myuser2),1004(mygroup)
   * id myuser3
      uid=1006(myuser3) gid=1008(myuser3) groups=1008(myuser3),1004(mygroup)
   * id nouser1
      uid=1007(nouser1) gid=1009(nouser1) groups=1009(nouser1),1005(nogroup)
   * id nouser2
      uid=1008(nouser2) gid=1010(nouser2) groups=1010(nouser2),1005(nogroup)
   * id nouser3
      uid=1009(nouser3) gid=1011(nouser3) groups=1011(nouser3),1005(nogroup)
4.建立/srv/myproject + 修改群組和權限
   (1)mkdir /srv/myproject
   (2)chgrp mygroup /srv/myproject
   (3)chmod 770 /srv/myproject
   (4)ls -ld /srv/myproject
      * drwxrwx---. 2 root mygroup 6 Oct 28 11:26 /srv/myproject
5.切換成myuser1，建立myuser1.data的檔案
   (1)su myuser1
   (2)cd /srv/myproject
   (3)vi myuser1.data
      * [Esc] :wq
6.複製 /usr/bin/ls到/usr/local/bin/myls
   (1)cp /usr/bin/ls /usr/local/bin/myls
   (2)ll /usr/local/bin/myls
      * -rwxr-xr-x. 1 root root 117672 Oct 28 11:46 /usr/local/bin/myls
7.切換身分nouser1
   su nouser1
   (1)第一次嘗試
    * ls : permission denied
    * ll /usr/local/bin/myls
       -rwxr-xr-x. 1 root root 117672 Oct 28 11:46 /usr/local/bin/myls
    * myls /srv/myproject : permission denied
  (2)第二次嘗試
     修改群組
    [root身分]
    * ll /usr/local/bin/myls
       -rwxr-xr-x. 1 root root 117672 Oct 28 11:46 /usr/local/bin/myls
    * chgrp mygroup /usr/local/bin/myls
    * ll /usr/local/bin/myls
       -rwxr-xr-x. 1 root mygroup 117672 Oct 28 11:46 /usr/local/bin/myls
    * su nouser1
    * myls /srv/myproject : permission denied
  (3)第三次嘗試
    [root身分]
    * sudo chmod u+s /usr/local/bin/myls
    * ll /usr/local/bin/myls
       -rwsr-xr-x. 1 root mygroup 117672 Oct 28 11:46 /usr/local/bin/myls
           檔名變成紅色
    * su nouser1
    * myls /srv/myproject
    * myuser1.data 成功切換
----------------------------------------------------

## 程序指令
1.利用grep 尋找rsyslog相關程序資料
  * PID:955
  * PR:20
  * NI:0
  * COMMAND:/usr/bin/rsyslogd -n
  (1)第一次嘗試
   * ps aux | grep rsyslog
   找出PID為955
   找出COMMAND為/usr/bin/rsyslogd -n
  (2)第二次嘗試
   * ps -l
   沒有找到相關資料
  (3)第三次嘗試
   * ps -1
   發現可以查詢該PID的資料
  (4)第四次嘗試
   * ps -955
   找出COMMAND為/usr/bin/rsyslogd -n
  (5)第五次嘗試
   * top
   找出PR為20
   找出NI為0
  (6)第六次嘗試
   * ps aux
   也找出PR為20
   找出NI為0
2.將剛剛找到的rsyslog的檔案儲存到/root/process_syslog.txt
  * ps aux | grep rsyslog > /root/process_syslog.txt
  * vi process_syslog.txt
     發現資料已存到檔案中
----------------------------------------------------

## find指令及操作
1.find /usr/bin /usr/sbin -perm /4000
   * SUID為4分
   * -perm /mode ：搜尋檔案權限『包含任一 mode 的權限』的檔案
2.find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;
   * -exec (指令) : 將檔案轉成(指令)，此題為轉成ls -l列出來
  特殊檔名:
   - chfn
   - chsh
   - mount
   - chage
   - gpasswd
   - newgrp
   - su
   - umount
   - sudo
   - pkexec
   - crontab
   - passwd
   - pam_timestamp_check
   - unix_chkpwd
   - usernetct1
3.存取檔案到findsuidsgid.txt
  * find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; >  /root/findsuidsgid.txt
  * vi findsuidsgid.txt
     發現資料已存到檔案中